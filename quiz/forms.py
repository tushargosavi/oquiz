import re
from django.contrib.auth.models import User
from django import forms;

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(
        label="Password",
        widget = forms.PasswordInput()
        )
    password2 = forms.CharField(
        label="Password (Again)",
        widget = forms.PasswordInput()
        )

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('Password do not match. ')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('User name can only contain alphanumeric characters and the underscore')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

class QuestionSaveForm(forms.Form):
    text = forms.CharField(
        label="Question",
        widget=forms.TextInput(attrs={'size' : 64})
        )
    opt1 = forms.CharField(
        label="Option 1",
        widget=forms.TextInput(attrs={'size' : 64}))
    opt2 = forms.CharField(
        label="Option 1",
        widget=forms.TextInput(attrs={'size' : 64}))
    opt3 = forms.CharField(
        label="Option 1",
        widget=forms.TextInput(attrs={'size' : 64}))
    opt4 = forms.CharField(
        label="Option 1",
        widget=forms.TextInput(attrs={'size' : 64}))
    ans = forms.IntegerField(label="Answer")
    tags = forms.CharField(
        label="Tags",
        required=False,
        widget=forms.TextInput(attrs={'size' : 64}))
