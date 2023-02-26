from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from auth_login.models import User
from .forms import ObjectModelForm
from .models import Order
from home.forms import AddressForm
from home.models import Address


@login_required(login_url='/login/')
@ensure_csrf_cookie
def upload(request):
    context = {}
    if request.method == "POST":
        form = ObjectModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            order = Order.objects.create(user=request.user, model=form.instance)
            return redirect('/checkout/' + order.name)
        else:
            context['form'] = form
    else:
        context['form'] = ObjectModelForm()
    return render(request, template_name="printing/upload.html", context=context)


@login_required(redirect_field_name="/login/")
@ensure_csrf_cookie
def checkout(request, order):
    # get or 404
    # order = Order.objects.get(id=order)
    # check if order exists and if it belongs to the user who is logged in else render 404
    order = Order.objects.filter(name=order, user=request.user).first()
    if not order:
        return render(request, template_name="404.html")
    context = {"object": order.model, "order": order, }
    address = Address.objects.filter(user=request.user).first()
    if address:
        context['address'] = address

    if request.method == "POST":
        form = AddressForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            order.address = form.instance
            order.price = 1000
            order.save()

            return redirect(f'/dashboard/orders/')
        else:
            print(form.errors)
            context['form'] = form
    else:
        context['form'] = AddressForm()
    return render(request, template_name="printing/checkout.html", context=context)
