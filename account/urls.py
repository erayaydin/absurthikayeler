from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^login/$', auth_views.login, { "template_name": "login.html" }, name="login"),
    url(r'^logout/', auth_views.logout, { "next_page": "/" }, name="logout"),
    url(r'^register/', views.register, name="register")
]