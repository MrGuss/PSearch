from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('search', views.home, name='home'),
    path('createDB', views.createDB, name='db'),
    path('autocomplete/', views.TeacherAutocomplete.as_view(), name='autocomplete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
