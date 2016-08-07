from django.shortcuts import *
from models import Blog
from .forms import RegisterForm,LoginForm
from django.contrib.auth import *
from django.http import *
from rest_framework.response import *
from django.contrib.auth.models import User
from blogapp.serializers import BlogSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def register(request):
    if request.method == 'POST':
        rform = RegisterForm(request.POST)
        if rform.is_valid():
            user = User.objects.create_user(rform.cleaned_data.get('username'),rform.cleaned_data.get('email'),rform.cleaned_data.get('password'))
            user.save()
        return render_to_response('static/blogproject/userhome.html')
    else:
        rform = RegisterForm()

    return render(request, 'static/blogproject/register.html', {'form': rform})

def user_login(request):
    if request.method == 'POST':
        lform = LoginForm(request.POST)
        if lform.is_valid():
            user = authenticate(username=lform.cleaned_data.get('username'),password=lform.cleaned_data.get('password'))
            if user :
                login(request,user)
                print("User is valid, active and authenticated")
            else:
                print("The username and password were incorrect.")
            return redirect('blogapp.views.userhome')
    else:
        lform = LoginForm()

    return render(request, 'static/blogproject/login.html', {'form': lform})

@csrf_exempt
def post(request):
    if (request.method=='POST'):
        data=JSONParser().parse(request)
        blog =  Blog()
        if(data['title'] and data['blogpost']):
            blog.title = data['title']
            blog.user = request.user
            blog.blogpost = data['blogpost']
            blog.save()
        return HttpResponseRedirect('/blog/userhome/',status=status.HTTP_200_OK)

def userhome(request):
    return render(request,'static/blogproject/userhome.html',{'user':request.user})

@api_view(['GET'])
def all_blogs(request):
    blogs = Blog.objects.all()
    b_s = BlogSerializer(blogs,many=True)
    return Response(b_s.data)


def newpost(request):
    return render_to_response('static/blogproject/newpost.html')