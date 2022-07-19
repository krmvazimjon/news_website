from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name = 'index'),
    # path('newsfor_detail/<int:pk>/', AboutPageView.as_view(), name = 'newsfor_detail')
    # path('category/', CategoryPageView.as_view(), name = 'category')
    path('newsfor_detail/<str:news_id>/', aboutPageView, name = 'newsfor_detail'),
    path('category/<int:category_id>/', catePageView, name = 'category')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)