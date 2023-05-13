from django.urls import path
from . import views
app_name='todo1app'

urlpatterns =[
    path('',views.home,name="home"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('clsview/',views.tasklist.as_view(),name="list"),
    path('clsdetail/<int:pk>/',views.taskdetail.as_view(),name="detail"),
    path('clsupdate/<int:pk>/',views.taskupdate.as_view(),name="clsup"),
    path('clsdelete/<int:pk>/',views.taskdelete.as_view(),name="clsdel"),

]