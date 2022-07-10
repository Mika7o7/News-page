from django.forms import ModelForm
from .models import News, Category


class CreateNews(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
