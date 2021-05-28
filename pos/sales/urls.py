from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
]
