from django.urls import path
from . import views

urlpatterns = [
    path('get_items/', views.item_list),
    path('get_items/<id>/', views.item_detail),
]