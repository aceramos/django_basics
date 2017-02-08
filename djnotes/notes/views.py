from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from .models import Notes

class Index(View):
    template_name = 'notes/index.html'

    def get_context_data(self):
        context = {
        'notes': Notes.objects.order_by('-id'),
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)