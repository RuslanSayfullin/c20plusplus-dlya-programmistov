from django import forms
from django.utils import timezone

from inquery.api import is_busy_datetime
from inquery.models import Inquery
from inquery.fields import PrettyModelChoiceField


class NewInqueryForm(forms.Form):
    designer = PrettyModelChoiceField(queryset=Inquery.designers.all(), widget=forms.Select(attrs={'class': 'selectpicker show-tick'}))
    name_client = forms.CharField(initial="")
    address_client = forms.CharField(initial="Респ Башкортостан, г Уфа,")
    porch_client = forms.CharField(required=False, initial="")
    phone_client = forms.CharField(initial="")
    phone_client_two = forms.CharField(required=False, initial="")
    room_client = forms.CharField(initial="")
    floor_client = forms.CharField(initial="")
    barter_coefficient = forms.CharField(required=False, initial="")
    type_production = forms.CharField(initial="")
    start_datetime = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], initial="")
    description = forms.CharField(required=False, initial="")
    source = forms.CharField(required=True, initial="")
    parent_inquery = forms.CharField(required=False, initial="")
    vtorichny = forms.BooleanField(required=False)

    def clean_start_datetime(self):
        start_datetime = self.cleaned_data['start_datetime']
        if start_datetime.minute == 30 or start_datetime.minute == 0:
            pass
        else:
            raise forms.ValidationError(u'Минуты должны быть равны 30 или 00')

        if start_datetime < timezone.now():
            raise forms.ValidationError(u"В прошлое позвонить нельзя")

        return self.cleaned_data['start_datetime']

    def clean_designer(self):
        designer = self.cleaned_data['designer']
        if not designer in Inquery.designers.all():
            raise forms.ValidationError(u'Такого дизайнера не существует')
        return self.cleaned_data['designer']

    def clean(self):
        cleaned_data = super(NewInqueryForm, self).clean()

        designer = cleaned_data.get('designer')
        start_datetime = cleaned_data.get('start_datetime')
        if is_busy_datetime(designer, start_datetime):
            self.add_error('start_datetime', u'На это время уже есть замер')

    class Media:
        css = {
            'all': (
                'datetimepicker/jquery.datetimepicker.css',
                'inquery/suggestions-4.10.css',
                'inquery/google_autocomplete/google_map_api_v3.css',
            )
        }
        js = (
            'jquery/dist/jquery.min.js',
            'jquery.inputmask/dist/jquery.inputmask.bundle.min.js',
            'inquery/inputmask_settings.js',
            'datetimepicker/jquery.datetimepicker.js',
            'inquery/datetimepicker_settings.js',
            'inquery/jquery.suggestions-4.10.min.js',
            'inquery/suggestions_settings.js',
            'inquery/google_autocomplete/google_map_api_v3.js',
            'inquery/google_autocomplete/google_map_settings.js',
        )
