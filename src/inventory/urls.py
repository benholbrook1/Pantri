from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list),
    path('<id>/', views.item_detail),
]