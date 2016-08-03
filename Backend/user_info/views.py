from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, Http404
from .models import user
# Create your views here.

def index(request):
    return render(request, '../templates/index.html')

def user_signup(request):
    if request.method == "POST":
        # form_class = UserForm(request.POST)
        # if form_class.is_valid():
        #     user = form_class.save(commit=False)
        #     password = make_password(form_class.cleaned_data.get('password'))
        #     user.password = password
        #     user.save()
        # return HttpResponse(password)
        username = request.POST['userid']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        num_result = user.objects.filter(email=email).count()
        if num_result == 0:
            nuser = user(email=email, alias=username, password=password)
            nuser.save()
        else:
            return HttpResponse("email already exist")

    return redirect(to='/')

def user_signin(request):
    if request.method == "POST":
        check_email = request.POST['email']
        try:
            result = user.objects.get(email=check_email)
        except result.DoesNotExist:
            return HttpResponse("dose not exist! " + result.email + " "+ check_email)
        else:
            check_pass = check_password(request.POST['password'], result.password)
            if check_pass is True:
                request.session["userid"] = result.id
                return redirect(to="/user/"+str(result.id))
            else:
                return HttpResponse("dose not exist! " + result.password)

def user_detail(request, userid):
    if request.session["userid"] == int(userid):
        try:
            result = user.objects.get(pk=userid)
        except result.DoesNotExist:
            return Http404

        if request.method == "GET":
            context = {
                "avatar": result.avatar,
                "email": result.email,
                "username": result.alias,
                "phonenumber": result.cellNumber
            }
        template = "../templates/user.html"
        return render(request, template, context)
    else:
        raise Http404("page not found"+str(request.session['userid']))