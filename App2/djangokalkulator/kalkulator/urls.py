from django.urls import path
from . import views

urlpatterns = [
    path('kalkulator/', views.ssl_info_view, name='kalkulator'),
]