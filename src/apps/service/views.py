from django.shortcuts import render
from apps.service.models import ServiceModel,PortfolioModel,CategoryModel
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

'''
def TestServiceView(request):
    return render(request,'service/seo.html')
'''

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