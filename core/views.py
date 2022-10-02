from logging import exception
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

from random import randint
from time import sleep

from .models import Topics


def login_render(request):

    try:

        return render(request, 'pages/login.html')

    except Exception as error:

        return HttpResponse("Error to process the page of login. Error: {}".format(error))

def create_user(request):
    try:
        if request.method == 'POST':

            unique_id = randint(0,777)  
            username = request.POST.get('user')
            password = request.POST.get('password')
            user = User.objects.filter(username=username).first()
            if user:
                return HttpResponse("Tjis user exist in us db")

            user = User.objects.create_user(username=username, password=password)
            user.save()
            return HttpResponse("Created user")


    except Exception as error:
        print(error)

def login_user(request):
    
    try:
        username = request.POST.get('user')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return HttpResponse('OK')
        else:
            return HttpResponse('NO')

    except Exception as error:
        print(error)

def logout_user(request):
    logout(request)
    return HttpResponse("Logout")

@login_required
def home(request):
    
    try:
        #if request.user.is_authenticated:

        topics = Topics.objects.all()
        return render(request, 'pages/index.html', {"topics":topics})
        #else:
        return HttpResponse('Precisa')
    except Exception as error:

        return HttpResponse(error)

def topics_view(request):
    try:
        
        topics = Topics.objects.all()
        return render(request, 'pages/topics.html', {"topics":topics})

    except Exception as error:
        
        return HttpResponse("Error in processing the topics page")

def save_data(request):
    
    try:
    
        if request.method == "POST":
            
                unique_id = randint(0,777)  
                name = request.POST.get("title")
                name2 = request.POST.get("text_topic")
                # dont call the function but the object profile
                accept = Topics(unique_id, name, name2)
                accept.save()
                return render(request,"pages/topics.html")

    except Exception as error:
        
        return HttpResponse("Error in processing the data. Try again...")

def update_render(request, p_key):
    
    try:
        
        topics = Topics.objects.get(p_key=p_key)
        return render(request, "pages/update.html", {"topics": topics})
    
    except Exception as error:
        
      print('Error in processing the topics page')        
    
def update_topic(request, p_key):
    
    try:
        
        if request.method == "POST":
            
                unique_id = p_key        
                name = request.POST.get("title")
                name2 = request.POST.get("text_topic")
                accept = Topics(unique_id, name, name2)
                accept.save()
                
                return render(request, 'pages/index.html')
            
    except Exception as error:
    
        print('Error in updated the topic'.format(error))        

def delete_render(request, p_key):
    
    try:
    
        topics = Topics.objects.get(p_key=p_key)
        return render(request, "pages/delete.html", {"topics": topics})
        
    except Exception as error:
      
        print('Error in render the topic'.format(error))        


def delete_topic(request, p_key):
    
    try:
        
        topics = Topics.objects.get(p_key=p_key)
        topics.delete()
        msg = "Successfully deleted! Waiting for 3 seconds... <"
        aa = render(request, "pages/index.html", {"topics": topics})
        return HttpResponse(aa)
    
    except Exception as error:
        
        print('Error in delete the topic'.format(error))        

    
    
