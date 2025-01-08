from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='Home'),
]