from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login',views.loginUserInWeb,name='login'),
    path('register',views.registerAction,name='register'),

]