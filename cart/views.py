from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.conf import settings
from decimal import Decimal
import iyzipay
from .forms import PaymentForm
from .models import Payment


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            card_holder_name = form.cleaned_data['card_holder_name']
            card_number = form.cleaned_data['card_number']
            expire_month = form.cleaned_data['expire_month']
            expire_year = form.cleaned_data['expire_year']
            cvc = form.cleaned_data['cvc']
            amount = form.cleaned_data['amount']

            options = {
                'api_key': settings.IYZICO_API_KEY,
                'secret_key': settings.IYZICO_SECRET_KEY,
                'base_url': settings.IYZICO_BASE_URL,
            }

            request_params = {
                'locale': 'tr',
                'conversationId': '123456789',
                'price': str(amount),
                'paidPrice': str(amount),
                'installment': 1,
                'basketId': 'B67832',
                'paymentChannel': 'WEB',
                'paymentGroup': 'PRODUCT',
                'paymentCard': {
                    'cardHolderName': card_holder_name,
                    'cardNumber': card_number,
                    'expireMonth': expire_month,
                    'expireYear': expire_year,
                    'cvc': cvc,
                    'registerCard': 0,
                },
                'buyer': {
                    'id': 'BY789',
                    'name': 'John',
                    'surname': 'Doe',
                    'gsmNumber': '+905350000000',
                    'email': 'email@email.com',
                    'identityNumber': '74300864791',
                    'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
                    'ip': '85.34.78.112',
                    'city': 'Istanbul',
                    'country': 'Turkey',
                    'zipCode': '34742',
                },
                'shippingAddress': {
                    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
                    'zipCode': '34742',
                    'city': 'Istanbul',
                    'country': 'Turkey',
                },
                'billingAddress': {
                    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
                    'zipCode': '34742',
                    'city': 'Istanbul',
                    'country': 'Turkey',
                },
                'basketItems': [
                    {
                        'id': 'BI101',
                        'name': 'Binocular',
                        'category1': 'Collectibles',
                        'category2': 'Accessories',
                        'price': str(amount),
                        'itemType': 'PHYSICAL',
                    },
                ],
            }

            try:
                payment_result = iyzipay.Payment.create(request_params, options)
                if payment_result.get('status') == 'success':
                    payment_obj = Payment.objects.create(
                        payment_id=payment_result.get('paymentId'),
                        status=payment_result.get('status'),
                        amount=Decimal(amount),
                    )
                    return redirect('payment_success')
                else:
                    return render(request, 'payment.html', {'form': form, 'error': payment_result.get('errorMessage')})
            except iyzipay.exceptions.iyzipayResourceError as e:
                return render(request, 'payment.html', {'form': form, 'error': str(e)})

    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})


def payment_success(request):
    return render(request, 'payment_success.html')
