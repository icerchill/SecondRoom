from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, Http404
from .models import user
from house.models import Room,Room_img
# Create your views here.

indexpage = '../templates/index.html'
userpage = '../templates/user.html'

def index(request):
    #roomdata = Room.objects.get()
    if 'username' in request.session:
        context = {
                    "user_status": "<a href='/house/roompost'>" + request.session["username"] + "</a>",
                    #"roomdata": roomdata
                }
        return render(request, indexpage, context)
    else:
        context = {
                    "user_status": "<a class='page-scroll' href='' data-toggle='modal' data-target='#myModal'>Login</a>",
                    #"roomdata": roomdata
                }
        return render(request, indexpage, context)

def user_signup(request):
    if request.method == "POST":
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
                request.session["username"] = result.alias
                return redirect(to="/")
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


def user_update(request, userid):
    if request.session["userid"] == int(userid):
        try:
            result = user.objects.get(pk=userid)
        except result.DoesNotExist:
            return Http404

        if request.method == "POST":
            result.cellNumber = request.POST()
        return redirect(to='/user/'+str(request.session["userid"]))
    else:
        raise Http404("page not found"+str(request.session['userid']))

def user_signout(request):
    request.session.flush()
    return redirect(to='/')