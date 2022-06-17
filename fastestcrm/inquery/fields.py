from django import forms


class PrettyModelChoiceField(forms.ModelChoiceField):
    # Show pretty user name
    def label_from_instance(self, user):
        user = user.get_full_name()
        return super(PrettyModelChoiceField, self).label_from_instance(user)