from apps.service.models import ServiceModel,PortfolioModel,CategoryModel
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from apps.public.forms import ContactUsForms
from django.views.generic import ListView
from .models import PortfolioModel, CategoryModel

class CategoryProductListView(ListView):
    model = PortfolioModel
    template_name = 'category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return PortfolioModel.objects.filter(category__id=category_id).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.get(id=self.kwargs['category_id'])
        return context

class PortfolioView(TemplateView):
    template_name = "service/portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.all()
        context['products'] = PortfolioModel.objects.all().order_by('-created_at')

        return context

class BaseServicePageView(TemplateView):
    template_name = ''
    service_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Social Media Marketing').first()
        context['content_create'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()

        context['service'] = ServiceModel.objects.filter(name__iexact=self.service_name).first()

        categories = CategoryModel.objects.filter(service__name__iexact=self.service_name)
        context['categories'] = categories

        latest_products_by_category = []
        for category in categories:
            latest_products = PortfolioModel.objects.filter(
                service__name__iexact=self.service_name,
                category=category
            ).order_by('-created_at')[:6]
            if latest_products.exists():
                latest_products_by_category.append({
                    'category': category,
                    'products': latest_products
                })

        context['latest_products_by_category']=latest_products_by_category

        context['form']=ContactUsForms

        return context


class ServiceDigitalMarketingPageView(BaseServicePageView):
    template_name = 'service/marketing.html'
    service_name = 'Digital Marketing'

class ServiceApplicationPageView(BaseServicePageView):
    template_name = 'service/application.html'
    service_name = 'Social Media Marketing'

class ServiceSeoPageView(BaseServicePageView):
    template_name = 'service/seo.html'
    service_name = 'SEO'

class ServiceWebPageView(BaseServicePageView):
    template_name = 'service/site.html'
    service_name = 'Web Development'



class ServiceContentCreationPageView(BaseServicePageView):
    template_name = 'service/content-creation.html'
    service_name = 'Content Creation'

class ServicePortfolioPageView(TemplateView):
        template_name = 'service/portfolio-page.html'
        service_name = ''

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            service_name = self.kwargs['service_name']
            service = ServiceModel.objects.filter(name__iexact=service_name).first()

            if service:
                context['service']: service
                context['products'] = PortfolioModel.objects.filter(service=service).order_by('-created_at').all()
            return context
