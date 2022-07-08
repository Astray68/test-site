from django.shortcuts import render
from MyTestWebsite.settings import EMAIL_HOST_USER
from .forms import ContactsForm
from django.views.generic.base import View
from contacts.tasks import send_mail_alert


class ContactsView(View):
    def get(self, request):
        form = ContactsForm()
        return render(request, 'contacts/contact.html', {'form':  form})

    def post(self, request):
        form = ContactsForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            full_message = f'Email: {email} ' \
                           f'Phone: {phone} ' \
                           f'First name: {first_name} ' \
                           f'Last name: {last_name} ' \
                           f'Message: {message}'
            recipient_email = ['astrayfr@gmail.com', 'stepanxolera8@gmail.com']
            send_mail_alert.delay('New contact', full_message, EMAIL_HOST_USER, recipient_email)
        return render(request, 'contacts/contact.html', {'form': form})
