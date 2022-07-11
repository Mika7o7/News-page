from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.HomeNews.as_view(),
        name='home',
    ),
    path(
        'create',
        views.add_news,
        name='create',
    ),
    path(
        'add_category',
        views.add_category,
        name='add_category',
    ),
    path(
        'news_ditail/<int:pk>',
        views.news_ditail,
        name='news_ditail',
    ),
    path(
        'category/<int:category_id>',
        views.NewsByCategory.as_view(),
        name='category',
    ),
    path(
        "register",
        views.register_request,
        name="register",
    ),
    path(
        "login",
        views.login_request,
        name="login",
    ),
    path(
        "logout",
        views.logout_request,
        name="logout",
    ),
    path(
        "password_reset",
        views.password_reset_request,
        name="password_reset",
    ),
]
