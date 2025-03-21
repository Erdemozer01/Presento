from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.views import generic
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import views
from base.models import Home


class LoginView(views.LoginView):
    template_name = 'registration/login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site = Home.objects.latest('created')
        context['site'] = get_current_site(self.request)
        context['site_name'] = site.name
        return context


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/sign-up.html'

    def get_success_url(self):
        return settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        messages.success(self.request, 'Hesabınız Başarılı şekilde oluşturuldu.')
        return super(RegisterView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site = Home.objects.latest('created')
        context['site'] = get_current_site(self.request)
        context['site_name'] = site.name
        return context


class LogoutView(views.LogoutView):
    template_name = 'registration/logged_out.html'

    def get_success_url(self):
        return redirect('logout')


class PasswordResetView(views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    def form_valid(self, form):
        settings.EMAIL_HOST_USER = Home.objects.latest('created').email
        settings.EMAIL_HOST_PASSWORD = Home.objects.latest('created').email_password
        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)


