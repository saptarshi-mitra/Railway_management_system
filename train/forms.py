from django import forms


class NameForm(forms.Form):
    start_station = forms.CharField(label='Origin', max_length=100)
    dest_station = forms.CharField(label='Destination', max_length=100)
