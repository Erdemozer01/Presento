from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('starter/', views.StarterView.as_view(), name='starter'),
    path('hizmetlerimiz/<slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('iletisim/', views.ContactView, name='contact'),
    path('subscriber/', views.SubscriberView, name='subscriber'),
    path('pricing/', views.PricingView.as_view(), name='pricing'),
]
