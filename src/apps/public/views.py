from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import NewsModel,ArticleModel,AboutModel,ReviewModel
from apps.account.models import ProfileTeam
from apps.service.models import ServiceModel,PortfolioModel
from django.shortcuts import render


def Test(request):
    return render(request,'public/test.html')


class HomePageView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_news'] = NewsModel.objects.all().order_by('-created_at')[:5]
        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Social Media Marketing').first()
        context['content_create'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()
        context['latest_portfolios'] = {
            'seo':PortfolioModel.objects.filter(service__name__iexact='SEO').order_by('-created_at').first(),
            'digital_marketing':PortfolioModel.objects.filter(service__name__iexact='Digital Marketing').order_by('-created_at').first(),
            'web_dev':PortfolioModel.objects.filter(service__name__iexact='Web Development').order_by('-created_at').first(),
            'social_media':PortfolioModel.objects.filter(service__name__iexact='Social Media Marketing').order_by('-created_at').first(),
        }
        context['latest_articles'] = ArticleModel.objects.order_by('-created_at')[:5]
        context['about'] = AboutModel.objects.first()
        context['latest_reviews'] = ReviewModel.objects.order_by('-created_at')[:5]

        return context

class ArticleListView(ListView):
    model = ArticleModel
    template_name = 'public/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return ArticleModel.objects.order_by('-created_at')

class ReviewListView(ListView):
    model = ReviewModel
    template_name = 'public/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return ReviewModel.objects.order_by('-created_at')

