from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from openstreetview.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from openstreetview.models import *
import datetime
import json

def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            username_ = form.cleaned_data['username']
            password_ = form.cleaned_data['password']
            email_ = form.cleaned_data['email']
            if User.objects.filter(username=username_).exists():
                form = register_form()
                error = "User Already Exists"
            else:
                u = User.objects.create_user(username_,email_, password_)
                u.is_active = True
                u.save()
                return HttpResponseRedirect('/')
        else:
            form = register_form()
            error = "Invalid Inputs"  
    else:
        form = register_form()
        error = ""

    return render(request, 'useform.html', {'form': form, 'error': error})

@login_required
def add_image(request):
    if request.method == 'POST':
        form = loc_form(request.POST)
        if form.is_valid():
            image_name_ = form.cleaned_data['docfile']
            x_loc_ = form.cleaned_data['loc_x']
            y_loc_ = form.cleaned_data['loc_y']
            img_add = image_data(image_path=image_name_, location_x=x_loc_, location_y=y_loc_,approvals=0)
            img_add.save()
            imgurl = 'http://127.0.0.1:3000/' + image_name_
            return render(request, "complete.html", { 'imgurl' : imgurl })
        else:
            return HttpResponse("naa!! -_-")
    else:
        return HttpResponse("ACCESS DISABLED")

@login_required
def imagelocation(request, image_name):
    form = loc_form(initial={'docfile': image_name})
    return render(request, "addimgform.html", { 'form': form})
    

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            ext = request.FILES['docfile'].name.split('.')[1]
            request.FILES['docfile'].name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.' + ext
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            newform = loc_form(initial={'docfile': request.FILES['docfile'].name })
            return render(request, "addimgform.html", { 'form': newform})
    else:
        form = DocumentForm()

    return render(request, 'uploadform.html', {'form':form})


def mapdata(request):
    imgdata = image_data.objects.all()
    data = serializers.serialize('json', imgdata, indent=2)
    return HttpResponse(data, content_type='application/json')

@login_required
def load_unapproved_images(request):
    unapprovedimages = image_data.objects.filter(approvals__lt = 2)
    return render(request, 'imageapproval.html', { 'images': unapprovedimages })

def approve_image(request):
    imglist = request.POST.getlist('approvedimages[]') 
    data = json.loads(request.body)
    for img in imglist:
        image = image_data.objects.get(id=img)
        image.approvals += 1
        image.save()
    return HttpResponseRedirect("/")


