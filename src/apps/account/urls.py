from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login',views.loginUserInWeb,name='login'),
    path('register',views.registerAction,name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('logout',views.LogOutUser,name='logout'),

]
