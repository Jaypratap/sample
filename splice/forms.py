from django import forms
from django.utils.translation import gettext as _
from .models  import vendor, bidder
from django.forms import ModelForm

class RegistrationForm1(ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)
    email_conf = forms.CharField(label='email')

    class Meta:
        model = bidder

        fields = ['firstName', 'lastName', 'email', 'password1', 'password2', 'companyName', 'mobile', 'telephone', 'addressline1',
                  'addressline2', 'city', 'postalzip', 'country', 'state', 'email_conf']

    def clean(self):
        self.error_messages = {"email_mismatch": _("Email Do Not Match"),
                               }
        email = self.cleaned_data.get('email')
        email_conf = self.cleaned_data.get('email_conf')
        try:
            if email and email_conf and email != email_conf:
                raise forms.ValidationError(self.error_messages['email_mismatch'], code='email_mismatch')
        except:
            return email

    def clean_password2(self):
        self.error_messages = {"password_mismatch": _("Password Do Not Match"),
                               }
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')
        if len(password1) < int(8):
            raise forms.ValidationError("This Password is to sort")
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm1, self).save(commit=False)
        user.firstNname = self.cleaned_data['firstName']
        user.lastName = self.cleaned_data['lastName']
        user.email = self.cleaned_data['email']
        user.companyName = self.cleaned_data['companyName']
        user.mobile = self.cleaned_data['mobile']
        user.telephone = self.cleaned_data['telephone']
        user.addressline1 = self.cleaned_data['addressline1']
        user.addressline2 = self.cleaned_data['addressline2']
        user.telephone = self.cleaned_data['telephone']
        user.city = self.cleaned_data['city']
        user.postalzip = self.cleaned_data['postalzip']
        user.country = self.cleaned_data['country']
        user.state = self.cleaned_data['state']
        user.password = self.cleaned_data['password2']

        if commit:
            user.save()

        return user

class RegistrationForm2(ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)
    email_conf = forms.CharField(label='email')

    class Meta:
        model = vendor

        fields = ['firstName', 'lastName', 'email', 'password1', 'password2', 'companyName', 'mobile', 'telephone', 'addressline1',
                  'addressline2', 'city', 'postalzip', 'country', 'state', 'email_conf']

    def clean(self):
        self.error_messages = {"email_mismatch": _("Email Do Not Match"),
                               }
        email = self.cleaned_data.get('email')
        email_conf = self.cleaned_data.get('email_conf')
        try:
            if email and email_conf and email != email_conf:
                raise forms.ValidationError(self.error_messages['email_mismatch'], code='email_mismatch')
        except:
            return email

    def clean_password2(self):
        self.error_messages = {"password_mismatch": _("Password Do Not Match"),
                               }
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')
        if len(password1) < int(8):
            raise forms.ValidationError("This Password is to sort")
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm2, self).save(commit=False)
        user.firstNname = self.cleaned_data['firstName']
        user.lastName = self.cleaned_data['lastName']
        user.email = self.cleaned_data['email']
        user.companyName = self.cleaned_data['companyName']
        user.mobile = self.cleaned_data['mobile']
        user.telephone = self.cleaned_data['telephone']
        user.addressline1 = self.cleaned_data['addressline1']
        user.addressline2 = self.cleaned_data['addressline2']
        user.telephone = self.cleaned_data['telephone']
        user.city = self.cleaned_data['city']
        user.postalzip = self.cleaned_data['postalzip']
        user.country = self.cleaned_data['country']
        user.state = self.cleaned_data['state']
        user.password = self.cleaned_data['password2']

        if commit:
            user.save()

        return user