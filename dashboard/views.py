from django.shortcuts import render
from django.views import generic

# Create your views here.
class Dashboard(generic.TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["dashboard_active"] ="active"
        return context   