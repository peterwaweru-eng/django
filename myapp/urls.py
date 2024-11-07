from django.urls import path
from  myapp import views

urlpatterns=[

    path('',views.home,name='my-home'),

    path('about/',views.about,name='my-about'),
    path('blogs/',views.blogs,name='blogs'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact')

]
