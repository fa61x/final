from . import views
from django.urls import path, re_path

urlpatterns = [

    path('', views.index, name='index'),
    path('sinup_page', views.sinup_page, name='sinup_page'),
    path('reg_page', views.reg_page, name='reg_page'),
    path("enquiry", views.enquiry, name="enquiry"),
    path("save_enq", views.save_enq, name="save_enq"),
    path("confirm", views.confirm, name="confirm"),


    re_path(r'^getCoursedetails/$', views.getCoursedetails, name='getCoursedetails'),

]
