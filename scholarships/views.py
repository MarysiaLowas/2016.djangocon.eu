from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .forms import ApplicationForm
from .models import Application


class LandingView(generic.CreateView):
    model = Application
    template_name = 'scholarships/landing.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('scholarships:thanks')


class ThankYouView(generic.TemplateView):
    template_name = 'scholarships/thanks.html'
