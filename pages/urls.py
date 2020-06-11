from django.urls import path
from .views import HomePageView,AboutPageView,contact
from message.views import MessageView

urlpatterns=[
    path('about/',AboutPageView.as_view(),name='about'),#about page url
    path('',HomePageView.as_view(),name='home'),#homepage url 
    path('request/',contact),#contact
    path('message/',MessageView.as_view(),name='message')#contact
]