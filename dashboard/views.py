from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from printing.models import Order


# Create your views here.
# edit user profile
@login_required(login_url='/login/')
def dashboard(request):

    return render(request, 'dashboard/dashboard.html')


@csrf_exempt
@login_required(login_url='/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'dashboard/edit_profile.html', args)


@login_required(login_url='/login/')
def pending_orders(request):
    orders = Order.objects.filter(status='pending', user=request.user).order_by('-id')
    context = {
        'orders': orders
    }
    return render(request, 'dashboard/orders.html')


@login_required(login_url='/login/')
def completed_orders(request):
    orders = Order.objects.filter(status='completed', user=request.user).order_by('-id')
    context = {
        'orders': orders
    }
    return render(request, 'dashboard/orders.html')
