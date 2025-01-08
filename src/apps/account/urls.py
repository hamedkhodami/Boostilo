from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('team/',views.TeamListView.as_view(),name='TeamListView'),
    path('team/',views.TeamPhotoListView.as_view(),name='TeamPhotoListView'),
]