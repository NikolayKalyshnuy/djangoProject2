from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    qwerty = forms.CharField(label='lab_qwerty')
