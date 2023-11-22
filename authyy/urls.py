from django.urls import path, include

from authyy import views

from django.contrib.auth import views as auth_views
from allauth.account.views import LogoutView


path('register', views.registerPage, name='register'),
path('accounts/', include('allauth.urls')),

path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
     name="reset_password"),
path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
     name="password_reset_done"),
path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset.html"),
     name="password_reset_confirm"),
path('reset_password_complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
     name="password_reset_complete"),


path('logout', LogoutView.as_view()),

