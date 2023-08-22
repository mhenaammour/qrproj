from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_qr, name='generateqr'),
    path('generate/', views.generate_qr, name='generate_qr'),
    path('scan/', views.scan_qr, name='scan_qr'),
]
