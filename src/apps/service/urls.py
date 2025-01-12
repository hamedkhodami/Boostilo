from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('',views.ServiceView,name='service'),
    path('services/<int:service_id>/',views.ServiceProductListVeiw.as_view(),name='service'),
    path('application/', views.ServiceApplicationPageView.as_view(), name='application'),
    path('seo/', views.ServiceSeoPageView.as_view(), name='seo'),
    path('web/', views.ServiceWebPageView.as_view(), name='web'),
    path('marketing/', views.ServiceDigitalMarketingPageView.as_view(), name='marketing'),
    path('content/', views.ServiceContentCreationPageView.as_view(), name='content'),

]