from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('',views.PortfolioView.as_view(),name='service'),
    path('service/<str:service_name>/',views.ServicePortfolioPageView.as_view(),name='service_portfolios'),
    path('category/<int:category_id>/',views.CategoryProductsView.as_view(), name='category_products'),
    path('application/', views.ServiceApplicationPageView.as_view(), name='application'),
    path('seo/', views.ServiceSeoPageView.as_view(), name='seo'),
    path('web/', views.ServiceWebPageView.as_view(), name='web'),
    path('marketing/', views.ServiceDigitalMarketingPageView.as_view(), name='marketing'),
    path('content/', views.ServiceContentCreationPageView.as_view(), name='content'),
    path('portfolio/<int:pk>/', views.DetailPortfolioView.as_view(), name='portfolio'),

]