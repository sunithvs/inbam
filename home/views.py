from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response

# from home.forms import OrderForm


# index view
class IndexView(TemplateView):
    template_name = 'home/index.html'

    # render index.html
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())



# class OrderViewSet(viewsets.ViewSet):
#
#     @staticmethod
#     def create(request):
#         form = OrderForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home:index')
#         return Response({'form': form})
#
#     @staticmethod
#     def list(request):
#         form = OrderForm()
#         return Response({'form': form})



