from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('report/<int:pk>/', views.report_view, name='report'),
]