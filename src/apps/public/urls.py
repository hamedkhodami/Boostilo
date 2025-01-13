from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('test/',views.Test,name='test'),
]