from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from printing.models import Order


# Create your views here.
# edit user profile
@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard/index.html')


@csrf_exempt
@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return HttpResponseRedirect('/dashboard/profile')


@login_required(login_url='/login/')
def pending_orders(request):
    orders = Order.objects.filter(status='pending', user=request.user).order_by('-id')
    context = {
        'orders': orders
    }

    return render(request, 'dashboard/order.html', context)


@login_required(login_url='/login/')
def completed_orders(request):
    orders = Order.objects.filter(status='completed', user=request.user).order_by('-id')
    context = {
        'orders': orders
    }
    return render(request, 'dashboard/order.html', context)
