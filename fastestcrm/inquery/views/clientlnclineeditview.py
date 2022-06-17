from django.http import JsonResponse
from django.views import generic

from inquery.models import Client, Inquery
from inquery.forms import ClientForm


class ClientInclineEditView(generic.edit.BaseFormView):
    http_method_names = ["post"]
    form_class = ClientForm
    client = None
    froze = None

    def get_form_kwargs(self):
        data = {}
        data["name_client"] = self.request.POST.get("name_client") or self.client.name
        data["address_client"] = self.request.POST.get("address_client") or self.client.address
        data["phone_client"] = self.request.POST.get("phone_client") or self.client.phone
        data["phone_client_two"] = self.request.POST.get("phone_client_two") or self.client.phone_two
        data["room_client"] = self.request.POST.get("room_client") or self.client.room
        data["floor_client"] = self.request.POST.get("floor_client") or self.client.floor
        data["porch_client"] = self.request.POST.get("porch_client") or self.client.porch
        data["type_production"] = self.request.POST.get("type_production") or self.froze.type_production
        return {'data': data}

    def form_valid(self, form):
        client_id = self.kwargs.get('client_id')
        form.save(int(client_id))
        return JsonResponse({"response": "ok"})

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors.as_json()}, status=400)

    def dispatch(self, *args, **kwargs):
        client_id = kwargs.get('client_id')
        client = Client.objects.filter(id=client_id)
        if not client:
            return JsonResponse({"response": "client {0} not found".format(client_id)}, status=404)
        if len(client) != 1:
            return JsonResponse({"response": "return multi client"}, status=400)
        self.client = client[0]

        self.froze = Inquery.objects.get(client=self.client)
        if self.request.user != self.froze.designer and not self.request.user.has_perm('froze.vozm_perenaznachat_dizajnerov_v_zayavkah'):
            return JsonResponse({"response": "not permission"}, status=403)
        if self.froze.status not in (Inquery.INQUERY_NEW, Inquery.INQUERY_REPEAT, Inquery.INQUERY_THINK):
            return JsonResponse({"response": "not permission"}, status=403)

        return super(ClientInclineEditView, self).dispatch(*args, **kwargs)
