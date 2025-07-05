from django.urls import path
from . import views

urlpatterns = [
    path('get_lists/', views.lists),
    path('get_lists/<id>/', views.lists_detail),
]