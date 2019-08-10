from django.urls import path

from . import views

urlpatterns = [
    path('', views.ColorBoardListView.as_view(), name="color-board-list"),
    path('game/<int:pk>/', views.ColorBoardDetailView.as_view(), name="color-board-view"),
    path('create/', views.ColorBoardCreateView.as_view(), name="color-board-create")
]
