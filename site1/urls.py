from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('blog/',views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('signin/',views.signin,name="signin"),
    path('ai/',views.ai,name="ai"),
    path('ml/',views.ml,name='ml'),
    path('nlp/',views.nlp,name='nlp'),
    path('dl/',views.dl,name='dl'),
    path('web/',views.web,name='web'),


]