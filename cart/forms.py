from django import forms

class PaymentForm(forms.Form):
    card_holder_name = forms.CharField(label="Kart Sahibi Adı")
    card_number = forms.CharField(label="Kart Numarası")
    expire_month = forms.CharField(label="Son Kullanma Ayı")
    expire_year = forms.CharField(label="Son Kullanma Yılı")
    cvc = forms.CharField(label="CVC")
    amount = forms.DecimalField(label="Tutar")