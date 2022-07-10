from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('create', add_news, name='create'),
    path('add_category', add_category, name='add_category'),
    path('news_ditail/<int:pk>', news_ditail, name='news_ditail'),
    path('category/<int:category_id>', NewsByCategory.as_view(),
         name='category'),
]
