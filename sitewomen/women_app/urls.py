from django.urls import path, re_path, register_converter
from .views import *
from .converters import *
from .views import page_not_found

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CategoryView.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', TagPostList.as_view(), name='tag'),
    path('edit/<int:pk>/', UpdatePage.as_view(), name='edit_page'),
    # path('delete/<slug:slug>/', DeletePage.as_view(), name='delete_page'),
    path('delete/<slug:slug>/', deletePage, name='delete_page')
]

