from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import *
import requests 
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# 1 - usul rasm cqariwdi databasedan
class HomePageView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'newsfor'

#2 - usul
# def IndexPageView(request):
#     newlar = News.objects.all()
#     context = {
#         "yangiliklar":newlar,
#     }
#     return render(request,'index.html',context)


# class AboutPageView(DetailView):
#     model = News
#     template_name = 'about.html'

def aboutPageView(request, news_id):
    xabar = News.objects.filter(id = news_id)
    yangilik = xabar[0]
    context = {
    "yangilik": yangilik
    }
    return render(request, 'post_detail.html', context)

# class CategoryPageView(TemplateView):
#     template_name = 'category.html'

def catePageView(request, category_id):
    categoriya_ucun = Category.objects.get(pk = category_id)
    yangilik = News.objects.filter(category_id = categoriya_ucun)
    context = {
    "categoriya_ucun": categoriya_ucun,
    "yangilik": yangilik
    }
    return render(request, 'category.html', context)