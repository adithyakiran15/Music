from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . models import Music
from . forms import MusicForm

# Create your views here.
def index(request):
    music=Music.objects.all()
    context={
        'music_list':music
    }
    return render(request,"index.html",context)
def detail(request,music_id):
    musicid=Music.objects.get(id=music_id)
    return render(request,'detail.html',{'Music':musicid})




def add_music(request):
    if request.method=='POST':
        name=request.POST.get('name')
        singer = request.POST.get('singer')
        tag = request.POST.get('tag')
        img = request.FILES['img']
        file = request.FILES['file']
        music_add=Music(name=name,singer=singer,tag=tag,img=img, file=file)
        music_add.save()
        return redirect('/')

    return render(request,'add_music.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid user")

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                url = reverse('musicapp:register')
                return HttpResponseRedirect(url)
            else:
                user = User.objects.create_user(username=username, password=password, )
                user.save();
                url = reverse('musicapp:login')
                return HttpResponseRedirect(url)


        else:
            messages.info(request, "password not matching")
            url = reverse('musicapp:register')
            return HttpResponseRedirect(url)
    else:

        return render(request, 'register.html')
