from django.shortcuts import render
from apps.service.models import ServiceModel,PortfolioModel,CategoryModel
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

def ServiceView(request):
    return render(request,'public/portfolio.html')

class ServiceProductListVeiw(ListView):
    model = PortfolioModel
    template_name = 'public/portfolio.html'
    context_object_name = 'products'

    def get_queryset(self):
        service_id = self.kwargs.get('service_id')
        return PortfolioModel.objects.filter(service_id=service_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_id = self.kwargs.get('service_id')
        context['service'] = get_object_or_404(ServiceModel, id=service_id)
        context['services'] = ServiceModel.objects.all()
        return context

class ServiceApplicationPageView(TemplateView):
    template_name = 'service/application.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Social Media Marketing').first()
        context['content_create'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()

        context['service'] = ServiceModel.objects.filter(name__iexact='Social Media Marketing').first()
        context['products'] = PortfolioModel.objects.filter(service__name__iexact='Social Media Marketing')

        categories = CategoryModel.objects.filter(service__name__iexact='Social Media Marketing')
        context['categories'] = categories
        context['even_categories'] = [category for category in categories if category.id % 2 == 0]
        context['odd_categories'] = [category for category in categories if category.id % 2 == 1]

        return context

class ServiceSeoPageView(TemplateView):
    template_name = 'service/seo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Social Media Marketing').first()
        context['content_create'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()

        context['service'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['products'] = PortfolioModel.objects.filter(service__name__iexact='SEO')

        categories = CategoryModel.objects.filter(service__name__iexact='SEO')
        context['categories'] = categories
        context['even_categories'] = [category for category in categories if category.id % 2 == 0]
        context['odd_categories'] = [category for category in categories if category.id % 2 == 1]

        return context

class ServiceWebPageView(TemplateView):
    template_name = 'service/site.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Social Media Marketing').first()
        context['content_create'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()

        context['service'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['products'] = PortfolioModel.objects.filter(service__name__iexact='Web Development')

        categories = CategoryModel.objects.filter(service__name__iexact='Web Development')
        context['categories'] = categories
        context['even_categories'] = [category for category in categories if category.id % 2 == 0]
        context['odd_categories'] = [category for category in categories if category.id % 2 == 1]

        return context

class ServiceDigitalMarketingPageView(TemplateView):
    template_name = 'service/marketing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Social Media Marketing').first()
        context['content_create'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()

        context['service'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['products'] = PortfolioModel.objects.filter(service__name__iexact='Digital Marketing')

        categories = CategoryModel.objects.filter(service__name__iexact='Digital Marketing')
        context['categories'] = categories
        context['even_categories'] = [category for category in categories if category.id % 2 == 0]
        context['odd_categories'] = [category for category in categories if category.id % 2 == 1]

        return context

class ServiceContentCreationPageView(TemplateView):
    template_name = 'service/content-creation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Social Media Marketing').first()
        context['content_create'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()

        context['service'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()
        context['products'] = PortfolioModel.objects.filter(service__name__iexact='Content Creation')

        categories = CategoryModel.objects.filter(service__name__iexact='Content Creation')
        context['categories'] = categories
        context['even_categories'] = [category for category in categories if category.id % 2 == 0]
        context['odd_categories'] = [category for category in categories if category.id % 2 == 1]

        return context