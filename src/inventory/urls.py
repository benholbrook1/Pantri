from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemList.as_view()),  ## full url = /api/items/
    path('<id>/', views.ItemDetail.as_view()),  ## full url = /api/items/<id>/
]