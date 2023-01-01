from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response


# index view
class IndexView(TemplateView):
    template_name = 'home/index.html'

    # render index.html
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())
