from django import forms
from .models import News, Category


class CreateNews(forms.Form):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control',
                                              'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
