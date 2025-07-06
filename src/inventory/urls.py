from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list),  ## full url = /api/items/
    path('<id>/', views.item_detail),  ## full url = /api/items/<id>/
]