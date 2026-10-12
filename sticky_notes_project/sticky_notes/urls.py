from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note-list'),
    path('note/<int:pk>/', views.note_detail, name='note-detail'),
    path('note/new/', views.note_create, name='note-create'),
    path('note/<int:pk>/edit/', views.note_update, name='note-update'),
    path('note/<int:pk>/delete/', views.note_delete, name='note-delete'),
]
