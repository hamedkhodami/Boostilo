from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('',views.accountest,name='accountest'),

]