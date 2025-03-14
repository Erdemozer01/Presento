from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import generic

from .forms import InboxForm

from .models.home import Home, Services, Contact, Subscriber
from .models.inbox import Inbox


class StarterView(generic.TemplateView):
    template_name = 'pages/starter-page.html'

    def get(self, request, *args, **kwargs):
        if Home.objects.exists():
            return redirect('base:home')

        return super().get(request, *args, **kwargs)


class HomePageView(generic.ListView):
    model = Home
    template_name = 'pages/index.html'

    def get(self, request, *args, **kwargs):
        try:
            obj = Home.objects.latest('created')
        except Home.DoesNotExist:
            return redirect('base:starter')
        return render(request, self.template_name)


class ServiceDetailView(generic.DetailView):
    model = Services
    template_name = 'pages/service-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services_list'] = Services.objects.all()
        return context


def ContactView(request):
    form = InboxForm(request.POST or None)
    obj = Contact.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            try:
                Inbox.objects.create(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    subject=form.cleaned_data['subject'],
                    message=form.cleaned_data['message']
                )
                messages.success(request, 'Mesajınız başarılı şekilde iletilmiştir.')
            except Exception as e:
                messages.error(request, e)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'form': form, 'obj': obj}
    return render(request, 'pages/contact.html', context)


def SubscriberView(request):
    email = request.POST.get('email', None)
    if Subscriber.objects.filter(email=email).exists():
        messages.info(request, "Zaten abonesiniz")
    else:
        Subscriber.objects.create(email=email)
        messages.success(request, "Bültenimize abone olduğunuz için teşekkür ederiz.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class PricingView(generic.TemplateView):
    template_name = 'pages/pricing.html'


