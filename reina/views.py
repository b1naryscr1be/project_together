from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView

from .models import Situation


class HomeView(TemplateView):
    template_name = 'reina/home.html'


class SituationListView(ListView, LoginRequiredMixin):
    model = Situation
    login_url = '/accounts/login/'

    def get_queryset(self):
        return Situation.objects.filter(user=self.request.user)


class SituationCreateView(CreateView):
    model = Situation
    fields = ['title', 'description', 'what_i_feel', 'what_i_think', 'what_i_do', 'what_i_want', 'pic']
