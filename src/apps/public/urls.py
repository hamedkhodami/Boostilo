from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('blog/',views.BlogPageView.as_view(),name='blog'),
    path('contactuss/',views.ContactUs.as_view(),name='contactuss'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contactus/',views.contact_us_view,name='contact_us'),
    path('contactus_seo/',views.contact_us_view_in_seo,name='contactus_seo'),
    path('article/<int:pk>/',views.ArticleDetailView.as_view(), name='article_detail'),
    path('news/<int:pk>/',views.NewsDetailView.as_view(), name='news_detail'),
]

