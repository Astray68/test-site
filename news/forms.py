from django import forms
from django.core.exceptions import ValidationError
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    start_date = forms.DateField(label="Enter a start date")
    end_date = forms.DateField(label="Enter a end date")

    def clean_renewal_date(self):
        date1 = self.cleaned_data['start_date']
        date2 = self.cleaned_data['end_date']

        if date2 < datetime.date.today() or date1 < datetime.date.today():
            raise ValidationError('Non-correct date interval')

        if date2 < date1:
            raise ValidationError('Non-correct date interval')

        return date1, date2
