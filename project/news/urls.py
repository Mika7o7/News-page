from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('create', add_news, name='create'),
    path('category/<int:category_id>', NewsByCategory.as_view(),
         name='category'),
]
