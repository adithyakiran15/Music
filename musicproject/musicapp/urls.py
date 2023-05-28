from django.urls import path, include

from . import views
app_name='musicapp'

urlpatterns = [
       path('',views.index,name='index'),
       path('music/<int:music_id>/',views.detail,name='detail'),
       path('add/', views.add_music, name='add_music'),
       path('register/', views.register, name='register'),
       path('login/', views.login, name='login'),
       path('logout/', views.logout, name='logout'),

]