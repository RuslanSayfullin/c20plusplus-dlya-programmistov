from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views import generic

from dogovora.models import Dogovor
from inquery.api import get_unique_uuid
from inquery.forms import NewInqueryForm
from inquery.models import Client, Inquery, InqueryStatus
from inquery.utils import get_sms_text2, send_sms
from staff.models import Staff


class NewInqueryView(generic.FormView):
    template_name = 'inquery/new_inquery.html'
    form_class = NewInqueryForm
    start_datetime = None

    def dispatch(self, *args, **kwargs):
        # <если у пользов. нет прав "Возможность создавать ВСЕМ новые заявки/события "РеПин"" & нет прав "Возможность создавать ТОЛЬКО СЕБЕ новые заявки/события "РеПин""
        if not self.request.user.has_perm('inquery.vozm_sozdavat_vsem_novye_zayavki_sobytiya_repin') and \
                not self.request.user.has_perm('inquery.vozm_sozdavat_tolko_sebe_novye_zayavki_sobytiya_repin'):
            raise PermissionDenied
        # </если у пользов. нет прав "Возможность создавать ВСЕМ новые заявки/события "РеПин"" & нет прав "Возможность создавать ТОЛЬКО СЕБЕ новые заявки/события "РеПин""
        return super(NewInqueryView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # <права доступа...
        if not self.request.user.has_perm('inquery.vozm_sozdavat_vsem_novye_zayavki_sobytiya_repin'):  # если у пользов. нет прав "Возможность создавать ВСЕМ новые заявки/события "РеПин""
            if self.request.user != form.cleaned_data['designer']:  # Себе ли создает дизайнер новую заявку
                raise PermissionDenied
        # </права доступа...
        client_param = dict()
        client_param['name'] = form.cleaned_data['name_client']
        client_param['address'] = form.cleaned_data['address_client']
        client_param['phone'] = form.cleaned_data['phone_client']
        client_param['phone_two'] = form.cleaned_data['phone_client_two']
        client_param['room'] = form.cleaned_data['room_client']
        client_param['floor'] = form.cleaned_data['floor_client']
        client_param['porch'] = form.cleaned_data['porch_client']
        client = Client(**client_param)
        client.save()

        inquery_param = dict()
        inquery_param['client'] = client
        inquery_param['owner'] = self.request.user
        inquery_param['designer'] = form.cleaned_data['designer']
        inquery_param['type_production'] = form.cleaned_data['type_production']
        inquery_param['description'] = form.cleaned_data['description']
        inquery_param['source'] = form.cleaned_data['source']
        inquery_param['status'] = Inquery.INQUERY_NEW
        inquery_param['vtorichny'] = form.cleaned_data['vtorichny']
        inquery = Inquery(**inquery_param)
        inquery.uuid = get_unique_uuid(Inquery)
        inquery.save()

        status_param = dict()
        status_param['inquery'] = inquery
        status_param['status'] = Inquery.INQUERY_NEW
        status_param['author'] = self.request.user
        status_param['start_datetime'] = form.cleaned_data['start_datetime']
        status = InqueryStatus(**status_param)
        status.save()

        self.start_datetime = form.cleaned_data['start_datetime']

        if self.request.POST.get('send_client_sms'):
            try:
                designer = form.cleaned_data['designer']
                staff = Staff.objects.get(user=designer)
                sms_message = get_sms_text2(staff, designer, self.start_datetime)
                send_sms(sms_message, form.cleaned_data['phone_client'])
            except ObjectDoesNotExist:
                pass

        if form.cleaned_data['parent_inquery']:
            """Создается заявка после нажатия кнопки 'Новая заявка на основе этой'"""
            try:
                parent_inquery = Inquery.objects.get(uuid=form.cleaned_data['parent_inquery'])
                copy_from_dogovor = Dogovor.objects.get(inquery=parent_inquery)
                Dogovor.objects.create(
                    inquery=inquery,
                    author=self.request.user,

                    passport_familiya=copy_from_dogovor.passport_familiya,
                    passport_imya=copy_from_dogovor.passport_imya,
                    passport_otchestvo=copy_from_dogovor.passport_otchestvo,

                    passport_birthday_date=copy_from_dogovor.passport_birthday_date,
                    passport_birthday_place=copy_from_dogovor.passport_birthday_place,
                    passport_seria=copy_from_dogovor.passport_seria,
                    passport_nomer=copy_from_dogovor.passport_nomer,
                    passport_kem_vydan=copy_from_dogovor.passport_kem_vydan,
                    passport_kogda_vydan=copy_from_dogovor.passport_kogda_vydan,
                    passport_kp=copy_from_dogovor.passport_kp,
                    adres_propiski=copy_from_dogovor.adres_propiski,
                    adres_ustanovki=copy_from_dogovor.adres_ustanovki,
                    doverennye_lica=copy_from_dogovor.doverennye_lica,
                    doverennye_lica_telefony=copy_from_dogovor.doverennye_lica_telefony,
                    dizaynerskoe_voznagrazhdenie=copy_from_dogovor.dizaynerskoe_voznagrazhdenie,
                    akciya=copy_from_dogovor.akciya,
                )
            except (Dogovor.DoesNotExist, Inquery.DoesNotExist):
                Dogovor.objects.create(inquery=inquery, author=self.request.user)
        else:
            Dogovor.objects.create(inquery=inquery, author=self.request.user)

        return super(NewInqueryView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(NewInqueryView, self).get_context_data(**kwargs)
        kwargs["designer"] = self.request.GET.get('designer')
        kwargs["start_datetime"] = self.request.GET.get('datetime')
        return kwargs

    def get_success_url(self):
        year = self.start_datetime.year
        month = self.start_datetime.month
        day = self.start_datetime.day
        return reverse_lazy("calendar_url", kwargs={'year': year, 'month': month, 'day': day})

    def get_initial(self):
        self.initial["designer"] = self.request.GET.get('designer')
        self.initial["start_datetime"] = self.request.GET.get('datetime')
        #
        self.initial["name_client"] = self.request.GET.get('name_client') if self.request.GET.get('name_client') else ""
        self.initial["phone_client"] = self.request.GET.get('phone_client') if self.request.GET.get('phone_client') else ""
        self.initial["phone_client_two"] = self.request.GET.get('phone_client_two') if self.request.GET.get('phone_client_two') else ""
        self.initial["address_client"] = self.request.GET.get('address_client') if self.request.GET.get('address_client') else "Респ Башкортостан, г Уфа,"
        self.initial["porch_client"] = self.request.GET.get('porch_client') if self.request.GET.get('porch_client') else ""
        self.initial["room_client"] = self.request.GET.get('room_client') if self.request.GET.get('room_client') else ""
        self.initial["floor_client"] = self.request.GET.get('floor_client') if self.request.GET.get('floor_client') else ""

        self.initial["type_production"] = self.request.GET.get('type_production') if self.request.GET.get('type_production') else ""
        self.initial["source"] = self.request.GET.get('source') if self.request.GET.get('source') else ""
        self.initial["description"] = self.request.GET.get('description') if self.request.GET.get('description') else ""

        self.initial["parent_inquery"] = self.request.GET.get('parent_inquery') if self.request.GET.get('parent_inquery') else ""
        #
        return super(NewInqueryView, self).get_initial()
