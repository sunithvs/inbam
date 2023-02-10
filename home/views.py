from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response


# from home.forms import OrderForm


# index view
class IndexView(TemplateView):
    template_name = 'home/index.html'
    service = [
        {
            "title": "Online 3d printing",
            "description": "3D printing services, utilizing state-of-the-art technology and a team of experts to deliver accurate, functional, and aesthetically pleasing prototypes and finished products."
        },
        {
            "title": "Contract manufacturing",
            "description": "We  offers contract manufacturing services to provide clients with a dependable and efficient solution for their component needs. Utilizing an optimized production process, Inbum delivers high-quality components in a timely and reliable manner."
        },
        {
            "title": "Rapid Prototyping",
            "description": "Inbum provides rapid prototyping services utilizing state-of-the-art 3D printing technology to deliver quick and accurate prototypes for testing and iteration. This allows clients to streamline their design process and bring their product to market faster."
        },
        {
            "title": "Metal Casting",
            "description": "Inbum offers metal casting services at a reasonable price, providing clients with high-quality cast metal products that meet their unique needs and specifications."
        }

    ]
    why_choose_us = [
        {
            "title": "Quality",
            "description": "We are committed to providing our customers with the highest quality products and services. We are dedicated to continuous improvement and innovation to ensure that we are always providing the best possible solutions for our customers."
        },
        {
            "title": "Reliability",
            "description": "We are committed to providing our customers with the highest quality products and services. We are dedicated to continuous improvement and innovation to ensure that we are always providing the best possible solutions for our customers."
        },
    ]

    # render index.html

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = self.service
        context['why_choose_us'] = self.why_choose_us
        return context

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
