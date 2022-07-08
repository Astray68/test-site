from phonenumbers import NumberParseException
from .models import Contact
from django import forms
from django.core.exceptions import ValidationError
import phonenumbers
from captcha.fields import CaptchaField


def valid_phone_number(value):
    try:
        z = phonenumbers.parse(value, None)
    except NumberParseException:
        raise ValidationError(
            '%(value)s is not a valid phone number',
            params={'value': value}
        )

    if not phonenumbers.is_valid_number(z):
        raise ValidationError(
            '%(value)s is not a valid phone number',
            params={'value': value}
        )


class ContactsForm(forms.ModelForm):
    phone = forms.CharField(validators=[valid_phone_number])
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
