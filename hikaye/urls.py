from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bookIndex, name='book_index'),
    url(r'^book/create$', views.newBook, name='book_create'),
    url(r'^book/create/(?P<parent_id>[0-9]+)$', views.newBook, name="book_create_from_parent"),
    url(r'^book/(?P<book_id>[0-9]+)$', views.bookShow, name='book_show'),
    url(r'^category/(?P<category_id>[0-9]+)$', views.categoryShow, name='category_show'),
]