from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('blog/',views.BlogPageView.as_view(),name='blog'),
    path('contactus/',views.contact_us_view,name='contact_us'),
    path('article/<int:pk>/',views.ArticleDetailView.as_view(), name='article_detail'),
]

