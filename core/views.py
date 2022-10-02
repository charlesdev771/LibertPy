from logging import exception
from django.shortcuts import render, redirect
from django.http import HttpResponse

from random import randint
from time import sleep

from .models import Topics


def login_render(request):

    try:

        return render(request, 'pages/login.html')

    except Exception as error:

        return HttpResponse("Error to process the page of login. Error: {}".format(error))

def home(request):
    
    try:
        
        topics = Topics.objects.all()
        return render(request, 'pages/index.html', {"topics":topics})

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

    
    
