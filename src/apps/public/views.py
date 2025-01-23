from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import NewsModel,ArticleModel,AboutModel,ReviewModel
from apps.service.models import ServiceModel,PortfolioModel
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactUsForms

def contact_us_view(request):
    if request.method == "POST":
        form = ContactUsForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect('public:home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactUsForms()

    return render(request, 'contactus.html', {'form': form})

class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'public/news_detail.html'
    context_object_name = 'news'

class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = 'public/article_detail.html'
    context_object_name = 'article'

class BlogPageView(TemplateView):
    template_name = 'public/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['blogs'] = ArticleModel.objects.order_by('-created_at')

        return context

class AboutView(TemplateView):
    template_name = 'public/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutModel.objects.first()

        return context


class HomePageView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_news'] = NewsModel.objects.all().order_by('-created_at')[:5]
        context['seo'] = ServiceModel.objects.filter(name__iexact='SEO').first()
        context['digital_marketing'] = ServiceModel.objects.filter(name__iexact='Digital Marketing').first()
        context['web_dev'] = ServiceModel.objects.filter(name__iexact='Web Development').first()
        context['social_media'] = ServiceModel.objects.filter(name__iexact='Application').first()
        context['content_create'] = ServiceModel.objects.filter(name__iexact='Content Creation').first()
        context['latest_portfolios'] = {
            'seo':PortfolioModel.objects.filter(service__name__iexact='SEO').order_by('-created_at').first(),
            'digital_marketing':PortfolioModel.objects.filter(service__name__iexact='Digital Marketing').order_by('-created_at').first(),
            'web_dev':PortfolioModel.objects.filter(service__name__iexact='Web Development').order_by('-created_at').first(),
            'social_media':PortfolioModel.objects.filter(service__name__iexact='Application').order_by('-created_at').first(),
        }
        context['latest_articles'] = ArticleModel.objects.order_by('-created_at')[:5]
        context['about'] = AboutModel.objects.first()
        context['latest_reviews'] = ReviewModel.objects.order_by('-created_at')[:5]

        return context




