from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie

from .forms import ObjectModelForm
from .models import Order


@login_required(login_url='/login/')
@ensure_csrf_cookie
def upload(request):
    context = {}
    if request.method == "POST":
        form = ObjectModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            Order.objects.create(user=request.user, model=form.instance)
            return redirect('/orders/?id=' + form.instance.name)
        else:
            context['form'] = form
    else:
        context['form'] = ObjectModelForm()
    return render(request, template_name="printing/upload.html", context=context)
