import string
from django import forms

from inquery.models import Client


class ClientForm(forms.Form):
    name_client = forms.CharField(initial="")
    address_client = forms.CharField(initial="Респ Башкортостан, г Уфа,")
    phone_client = forms.CharField(initial="")
    phone_client_two = forms.CharField(required=False, initial="")
    room_client = forms.CharField(initial="")
    floor_client = forms.CharField(initial="")
    porch_client = forms.CharField(required=False, initial="")
    type_production = forms.CharField(required=False, initial="")

    def clean_phone_client(self):
        phone = self.cleaned_data.get('phone_client')
        if not self._is_valid_phone(phone):
            raise forms.ValidationError(u"Не верна длина номера телефона")
        return self.cleaned_data.get('phone_client')

    def clean_phone_client_two(self):
        phone = self.cleaned_data.get('phone_client_two')
        if not phone:
            return self.cleaned_data.get('phone_client_two')
        if not self._is_valid_phone(phone):
            raise forms.ValidationError(u"Не верна длина номера телефона")
        return self.cleaned_data.get('phone_client_two')

    def _is_valid_phone(self, phone):
        PHONE_LENGTH = 11
        phone = "".join((i for i in phone if i in string.digits))
        if len(phone) != PHONE_LENGTH:
            return False
        return True

    def save(self, client_id):
        client = Client.objects.get(id=client_id)
        client.name = self.cleaned_data.get('name_client')
        client.address = self.cleaned_data.get('address_client')
        client.phone = self.cleaned_data.get('phone_client')
        client.phone_two = self.cleaned_data.get('phone_client_two')
        client.room = self.cleaned_data.get('room_client')
        client.floor = self.cleaned_data.get('floor_client')
        client.porch = self.cleaned_data.get('porch_client')
        client.save()
        inquery = client.inquery_set.all()[0]
        inquery.type_production = self.cleaned_data.get('type_production')
        inquery.save()
