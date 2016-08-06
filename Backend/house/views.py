from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from user_info.models import user
from .models import Room, Room_img
from .forms import RoomForm, ImageForm
from django.forms import modelformset_factory
from django.contrib import messages
from django.template import RequestContext

# Create your views here.

def roompost(request):
    ImageFormSet = modelformset_factory(Room_img,form=ImageForm)
    if request.method == 'POST':
        roomForm = RoomForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Room_img.objects.none())
        if roomForm.is_valid() and formset.is_valid():
            human = True
            post_form = roomForm.save(commit=False)
            post_form.User = user.objects.get(pk=request.session["userid"])
            post_form.save()
            for form in formset.cleaned_data:
                image = form
                photo = Room_img(room=post_form, image=image['image'])
                photo.save()
            return redirect("/")
        else:
            print roomForm.errors, formset.errors
    else:
        roomForm = RoomForm()
        formset = ImageFormSet(queryset=Room_img.objects.none())
    return render(request, 'roomupload.html',{'roomForm': roomForm, 'formset': formset},context_instance=RequestContext(request))