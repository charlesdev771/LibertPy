from django.contrib import admin
from django.urls import path, include

from .views import home, topics_view, update_render, delete_render, login_render
from .views import save_data, update_topic, delete_topic

urlpatterns = [
    
    path('login/', login_render, name='login_render'),
    path('home/', home, name='home'),
    path('topics_view/', topics_view, name='topics_view'),
    path("update_render/<int:p_key>/", update_render, name='update_render'),
    path("delete_render/<int:p_key>/", delete_render, name='delete_render'),

    path("save_data/", save_data, name='save_data'),
    path('update/<int:p_key>/', update_topic, name='update_topic'),
    path("delete_topic/<int:p_key>/", delete_topic, name='delete_topic'),
    
]
