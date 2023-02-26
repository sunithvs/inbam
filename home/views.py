from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .permissions import IsAuthenticated, IsOwner

from home.models import Address
from home.serializer import AddressSerializer


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


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request):
    return render(request, '500.html')


class ServiceView(TemplateView):
    template_name = 'home/service.html'
    service = {
        "direct-manufacturing": {
            "online-3d-printing": {
                "title": "Online 3d printing",
                "description": "3D printing services, utilizing state-of-the-art technology and a team of experts to deliver accurate, functional, and aesthetically pleasing prototypes and finished products."
                ,"about": "Using Imbam there is no minimum order quantity, from a single object to 10 000+ parts, you can 3D print the exact amount of parts you need. This is why additive manufacturing is particularly adapted to the creation of limited editions."
            },
        },
        "solutions": {
            "contract-manufacturing": {
                "title": "Contract manufacturing",
                "description": "We  offers contract manufacturing services to provide clients with a dependable and efficient solution for their component needs. Utilizing an optimized production process, Inbum delivers high-quality components in a timely and reliable manner."
            },
            "rapid-prototyping": {
                "title": "Rapid Prototyping",
                "description": "Inbum provides rapid prototyping services utilizing state-of-the-art 3D printing technology to deliver quick and accurate prototypes for testing and iteration. This allows clients to streamline their design process and bring their product to market faster."

            },
            "online-3d-printing": {
                "title": "Online 3d printing",
                "description": "3D printing services, utilizing state-of-the-art technology and a team of experts to deliver accurate, functional, and aesthetically pleasing prototypes and finished products."
            },

        }}

    def get_context_data(self, service_name, service_type, **kwargs):
        context = super(ServiceView, self).get_context_data(**kwargs)
        context['service'] = self.service.get(service_name).get(service_type)
        context["gold"] = service_name == "inbam-gold"
        return context

    def get(self, request, *args, **kwargs):
        service_name = kwargs.get('service_name')
        service_type = kwargs.get('type')
        print(service_name)
        if service_name not in self.service or service_type not in self.service.get(service_name):
            return redirect('index')
        return self.render_to_response(self.get_context_data(service_name, service_type))
