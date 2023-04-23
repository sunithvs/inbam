from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .permissions import IsAuthenticated, IsOwner

from home.models import Address
from home.serializer import AddressSerializer

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

service = [
        {
            "title": "Online 3d printing",
            "description": "Our skilled professionals leverage cutting-edge technology to produce precise and visually appealing prototypes and finished products for individuals and businesses. We provide convenient access to a variety of materials, including plastics, metals, and ceramics."
        },
        {
            "title": "Contract manufacturing",
            "description": "At inbam, we offer efficient contract manufacturing services to fulfill our clients' component requirements. Our optimized process guarantees the delivery of top-notch components that comply with unique specifications."
        },
        {
            "title": "Rapid Prototyping",
            "description": "We leverage 3D printing to produce swift and precise prototypes for testing and iteration. This streamlines the design process and accelerates product launches for our clients. Our service maximizes efficiency and shortens the product development cycle."
        },
        {
            "title": "Metal Casting",
            "description": "inbam delivers timely and reliable solutions for metal casting needs. Our team provides high-quality, cost-effective cast metal products that fulfill specific requirements. We maintain rigorous quality control standards to ensure consistently superior results."
        }

    ]

class IndexView(TemplateView):
    template_name = 'home/index.html'



    # render index.html

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = service
        context['why_choose_us'] = why_choose_us
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
                "description": "3D printing services, utilizing state-of-the-art technology and a team of experts to deliver accurate, functional, and aesthetically pleasing prototypes and finished products.",
                "about": "inbam is an online 3D printing service that offers high-quality, affordable 3D printing services to individuals and businesses worldwide. With inbam, you can upload your 3D design files and have them printed in a variety of materials, including PLA, ABS, PETG, and more. We use the latest 3D printing technology and techniques to ensure that your prints come out with the highest level of accuracy and detail possible. Our team of experts is dedicated to providing you with a seamless printing experience, from the moment you upload your design to the final product delivery. Whether you need a single prototype or thousands of parts, inbam is your go-to source for 3D printing services. Try our services today and see the difference that inbam can make for your project!"
            },
        },
        "solutions": {
            "contract-manufacturing": {
                "title": "Contract manufacturing",
                "description": "We  offers contract manufacturing services to provide clients with a dependable and efficient solution for their component needs. Utilizing an optimized production process, inbam delivers high-quality components in a timely and reliable manner."
                ,"about":"Imbam's contract-manufacturing service offers a reliable and efficient solution for businesses looking to outsource their manufacturing needs. With our state-of-the-art facilities and experienced team, we provide a wide range of manufacturing services, including CNC machining, injection molding, sheet metal fabrication, and more. We work closely with our clients to understand their specific requirements and tailor our services to meet their unique needs. Our goal is to provide our clients with high-quality products and services that meet or exceed their expectations, while also offering competitive pricing and timely delivery. Imbam's contract-manufacturing service is your partner for success in the manufacturing industry. Contact us today to learn more about how we can help you streamline your manufacturing processes and achieve your business goals."
            },
            "rapid-prototyping": {
                "title": "Rapid Prototyping",
                "description": "inbam provides rapid prototyping services utilizing state-of-the-art 3D printing technology to deliver quick and accurate prototypes for testing and iteration. This allows clients to streamline their design process and bring their product to market faster."
                ,"about":"Rapid prototyping is a cutting-edge technology that allows designers and engineers to quickly and easily create physical prototypes of their designs. This process involves using 3D printing, CNC machining, or other techniques to produce a physical model of a product, allowing designers to evaluate and refine their designs before moving into full-scale production. At Imbam, we specialize in rapid prototyping services and use the latest technology and techniques to ensure that your prototypes are produced with the highest level of accuracy and detail possible. Whether you need a single prototype or a batch of prototypes, our team of experts is dedicated to providing you with a seamless and efficient prototyping experience. With rapid prototyping, you can reduce your development time, improve your product design, and ultimately bring your products to market faster. Contact us today to learn more about our rapid prototyping services and how we can help you turn your ideas into reality."
            },
            "online-3d-printing": {
                "title": "Online 3d printing",
                "description": "3D printing services, utilizing state-of-the-art technology and a team of experts to deliver accurate, functional, and aesthetically pleasing prototypes and finished products.",
                "about": "Using Imbam, there is no minimum order quantity, from a single object to 10 000+ parts, you can 3D print the exact amount of parts you need. This is why additive manufacturing is particularly adapted to the creation of limited editions."

            },
            "on-demand-manufacturing": {
                "title": "On demand manufacturing",
                "description": "inbam offers on-demand manufacturing services to provide clients with a reliable and efficient solution for their component needs. Utilizing an optimized production process, inbam delivers high-quality components in a timely and reliable manner."
                ,"about":"On-demand manufacturing is a revolutionary approach to manufacturing that allows businesses to quickly and easily produce high-quality products in small or large quantities. At inbam, we offer on-demand manufacturing services that utilize advanced technology and manufacturing techniques to produce custom parts, components, and products with a fast turnaround time. Our on-demand manufacturing services include CNC machining, 3D printing, injection molding, sheet metal fabrication, and more. With our on-demand manufacturing services, you can streamline your production processes, reduce your inventory costs, and respond quickly to changing market demands. Our team of experts is dedicated to providing you with the highest level of service and quality, ensuring that your products are produced to your exact specifications. Contact us today to learn more about our on-demand manufacturing services and how we can help you take your business to the next level."
            }


        },

        "additive-manufacturing": {
            "design-studio":{
                "title": "Design studio",
                "description": "inbam offers a wide range of design services, including 3D modeling, 3D scanning, and 3D printing, to help you bring your ideas to life. Our team of experts is dedicated to providing you with a seamless and efficient design experience, from the initial concept to the final product delivery.",
                "about":"On Design Studio is inbam's design services division, dedicated to providing businesses with innovative and customized product design solutions. Our experienced design team works closely with our clients to understand their unique needs and develop creative and effective design solutions that meet or exceed their expectations. Our design services include product design, industrial design, prototyping, CAD modeling, and more. We use the latest design software and technology to ensure that our designs are accurate, detailed, and visually stunning. At On Design Studio, we are committed to providing our clients with exceptional design services that help them achieve their business goals. Contact us today to learn more about our design services and how we can help you bring your ideas to life."
            },

            "consulting":{
                "title": "Consulting",
                "description": "inbam offers a wide range of design services, including 3D modeling, 3D scanning, and 3D printing, to help you bring your ideas to life. Our team of experts is dedicated to providing you with a seamless and efficient design experience, from the initial concept to the final product delivery.",
                "about":"On Consulting is inbam's consulting services division, providing businesses with expert advice and guidance on a range of manufacturing and product development issues. Our team of consultants has extensive experience in the manufacturing industry, and can help you with everything from supply chain management and production optimization to quality control and regulatory compliance. Our consulting services are designed to help businesses of all sizes and industries improve their operational efficiency, reduce costs, and increase profitability. We work closely with our clients to understand their unique needs and develop customized solutions that are tailored to their specific requirements. At On Consulting, we are committed to providing our clients with the highest level of service and expertise, helping them achieve their business goals and succeed in today's competitive marketplace. Contact us today to learn more about our consulting services and how we can help you optimize your manufacturing processes and achieve success."
            }
        },

        "inbam-gold": {
            "online-3d-printing": {
                "title": "Online 3d printing",
                "description": "3D printing services, utilizing state-of-the-art technology and a team of experts to deliver accurate, functional, and aesthetically pleasing prototypes and finished products.",
                "about": "Using Imbam, there is no minimum order quantity, from a single object to 10 000+ parts, you can 3D print the exact amount of parts you need. This is why additive manufacturing is particularly adapted to the creation of limited editions."

            },
            "consulting":{
                "title": "Consulting",
                "description": "inbam offers a wide range of design services, including 3D modeling, 3D scanning, and 3D printing, to help you bring your ideas to life. Our team of experts is dedicated to providing you with a seamless and efficient design experience, from the initial concept to the final product delivery.",
                "about":"On Consulting is inbam's consulting services division, providing businesses with expert advice and guidance on a range of manufacturing and product development issues. Our team of consultants has extensive experience in the manufacturing industry, and can help you with everything from supply chain management and production optimization to quality control and regulatory compliance. Our consulting services are designed to help businesses of all sizes and industries improve their operational efficiency, reduce costs, and increase profitability. We work closely with our clients to understand their unique needs and develop customized solutions that are tailored to their specific requirements. At On Consulting, we are committed to providing our clients with the highest level of service and expertise, helping them achieve their business goals and succeed in today's competitive marketplace. Contact us today to learn more about our consulting services and how we can help you optimize your manufacturing processes and achieve success."
            },
            "design-studio":{
                "title": "Design studio",
                "description": "inbam offers a wide range of design services, including 3D modeling, 3D scanning, and 3D printing, to help you bring your ideas to life. Our team of experts is dedicated to providing you with a seamless and efficient design experience, from the initial concept to the final product delivery.",
                "about":"On Design Studio is inbam's design services division, dedicated to providing businesses with innovative and customized product design solutions. Our experienced design team works closely with our clients to understand their unique needs and develop creative and effective design solutions that meet or exceed their expectations. Our design services include product design, industrial design, prototyping, CAD modeling, and more. We use the latest design software and technology to ensure that our designs are accurate, detailed, and visually stunning. At On Design Studio, we are committed to providing our clients with exceptional design services that help them achieve their business goals. Contact us today to learn more about our design services and how we can help you bring your ideas to life."
            }
        }




    }

    def get_context_data(self, service_name, service_type, **kwargs):
        context = super(ServiceView, self).get_context_data(**kwargs)
        context['service'] = self.service.get(service_name).get(service_type)
        print(context['service'])
        context['why_choose_us'] = why_choose_us
        context['services'] = service
        context["gold"] = service_name == "inbam-gold"
        return context

    def get(self, request, *args, **kwargs):
        service_name = kwargs.get('service_name')
        service_type = kwargs.get('type')
        print(service_name)
        if service_name not in self.service or service_type not in self.service.get(service_name):
            return redirect('index')
        return self.render_to_response(self.get_context_data(service_name, service_type))
