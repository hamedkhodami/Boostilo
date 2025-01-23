from apps.service.models import ServiceModel,PortfolioModel,CategoryModel
from django.views.generic.base import TemplateView
from apps.public.forms import ContactUsForms
from .models import PortfolioModel, CategoryModel

class CategoryProductsView(TemplateView):
    template_name = 'service/portfolio-in-category-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = kwargs.get('category_id')
        category = CategoryModel.objects.get(id=category_id)
        products = PortfolioModel.objects.filter(category=category).order_by('-created_at')

        context['category'] = category
        context['products'] = products
        return context

class BaseServicePageView(TemplateView):
    template_name = ''
    service_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Application').first()
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

class PortfolioView(TemplateView):
    template_name = "service/portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.all()
        context['products'] = PortfolioModel.objects.all().order_by('-created_at')

        return context

class ServiceDigitalMarketingPageView(BaseServicePageView):
    template_name = 'service/marketing.html'
    service_name = 'Digital Marketing'

class ServiceApplicationPageView(BaseServicePageView):
    template_name = 'service/application.html'
    service_name = 'Application'

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
                context['service'] = service
                context['products'] = PortfolioModel.objects.filter(service=service).order_by('-created_at').all()
            return context
