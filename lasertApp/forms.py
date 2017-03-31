from captcha.fields import ReCaptchaField
from django import forms
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _

from lasertApp.models import Mailer


class ContactUsForm(forms.Form):
    STATUS_CHOICES=[('1',_("New Customer")),('2',_("Sales Service"))]
    to = forms.ChoiceField(choices = STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    contact_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact_email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact_phone = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control','rows':'6'})
    )

    captcha = ReCaptchaField(attrs={'theme' : 'clean'},required=True)

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = _("Your name")
        self.fields['contact_email'].label = _("Your email")
        self.fields['contact_phone'].label = _("Your phone")
        self.fields['content'].label = _("What do you want to say?")

    def send_email(self):
        mailList = list(Mailer.objects.filter(group=self.cleaned_data['to']).values('email'))
        #
        # Email the profile with the
        # contact information
        template =get_template('contact_template.txt')
        context = {'contact_name': self.cleaned_data['contact_name'],
                   'contact_email': self.cleaned_data['contact_email'],
                   'form_content': self.cleaned_data['content'],
                   'contact_phone': self.cleaned_data['contact_phone']
                    }
        content = template.render(context)
        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            mailList,
            headers={'Reply-To': self.cleaned_data['contact_email']}
        )
        email.send()





