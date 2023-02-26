from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from .forms import ObjectModelForm


@login_required(login_url='/login/')
@ensure_csrf_cookie
def index(request):
    context = {}
    if request.method == "POST":
        form = ObjectModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context['form'] = form
    else:
        context['form'] = ObjectModelForm()
    return render(request, template_name="printing/upload.html", context=context)
