from django import forms


class InboxForm(forms.Form):
    name = forms.CharField(label='Ad Soyad', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad Soyad', 'autocomplete': 'off'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}))
    subject = forms.CharField(label='Konu', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Konu', 'autocomplete': 'off'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mesaj', 'autocomplete': 'off'}))


class SubscribeForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}))
