"""
URL configuration for djangoProject5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from allauth.account.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from authyy import views
from authyy.views import about_view, ProductsView, AddToCartView, CartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.registerPage, name='register'),
    path('', views.loginpage, name='login'),
    path('accounts/', views.loginpage, name='loginpage'),
    path('soko/fresh/index/', views.index_view, name='fresh_index'),
    path('soko/fresh/about/', views.about_view, name='about_view'),
    path('soko/fresh/cart/', views.cart_view, name='cart_view'),
    path('soko/fresh/news/', views.news_view, name='news_view'),
    path('soko/fresh/single-news/', views.single_news_view, name='single-news_view'),
    path('soko/fresh/index_2/', views.index_view_2, name='index_2_view'),
    path('soko/fresh/checkout/', views.cart_view, name='checkout_view'),

    path('index/', ProductsView.as_view(), name='productlist'),

    path('accounts/', include('allauth.socialaccount.urls')),
    path('accounts/', include('allauth.urls')),

    # Define your URL pattern

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset.html"),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_complete"),

    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart_view'),

    path('logout',LogoutView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)