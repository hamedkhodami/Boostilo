from apps.service.models import ServiceModel,PortfolioModel,CategoryModel
from django.views.generic.base import TemplateView

class PortfolioView(TemplateView):
    template_name = "service/portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.all()
        context['products'] = PortfolioModel.objects.all()

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
        context['products'] = PortfolioModel.objects.filter(service__name__iexact=self.service_name)

        categories = CategoryModel.objects.filter(service__name__iexact=self.service_name)
        context['categories'] = categories

        return context

class ServiceApplicationPageView(BaseServicePageView):
    template_name = 'service/application.html'
    service_name = 'Social Media Marketing'

class ServiceSeoPageView(BaseServicePageView):
    template_name = 'service/seo.html'
    service_name = 'SEO'

class ServiceWebPageView(BaseServicePageView):
    template_name = 'service/site.html'
    service_name = 'Web Development'

class ServiceDigitalMarketingPageView(BaseServicePageView):
    template_name = 'service/marketing.html'
    service_name = 'Digital Marketing'

class ServiceContentCreationPageView(BaseServicePageView):
    template_name = 'service/content-creation.html'
    service_name = 'Content Creation'
