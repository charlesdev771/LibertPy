from django.contrib import admin
from django.urls import path, include

from .views import home, topics_view, update_render, delete_render, login_render, view_detail
from .views import save_data, update_topic, delete_topic, create_user, login_user, logout_user, make_comment

urlpatterns = [
    
    path('login/', login_render, name='login_render'),
    path('home/', home, name='home'),
    path('topics_view/', topics_view, name='topics_view'),
    path("update_render/<int:p_key>/", update_render, name='update_render'),
    path("delete_render/<int:p_key>/", delete_render, name='delete_render'),
    path('logout_user/',  logout_user, name="logout_user"),
    path('view_detail/<int:p_key>', view_detail, name="view_detail"),


    path("create_user/", create_user, name="create_user"),
    path("login_user/", login_user, name="login_user"),
    path("save_data/", save_data, name='save_data'),
    path('update/<int:p_key>/', update_topic, name='update_topic'),
    path("delete_topic/<int:p_key>/", delete_topic, name='delete_topic'),
    path("make_comment/<int:p_key>/", make_comment, name='make_comment'),
]
