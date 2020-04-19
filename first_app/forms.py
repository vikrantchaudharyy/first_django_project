from django import forms
from django.core import validators

from first_app.models import User, AccessRecord

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("ERROR: name should start with letter 'z'")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    # name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    bootcatcher = forms.CharField(required=False,
                                    widget=forms.HiddenInput,
                                    validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")


class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

class FormAccessRecord(forms.ModelForm):
    class Meta():
        model = AccessRecord
        fields = '__all__'
