from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('box/create/', views.create_box, name='create_box'),
    path('box/<int:box_id>/', views.view_box, name='view_box'),
    path('box/<int:box_id>/edit/', views.edit_box, name='edit_box'),
    path('box/<int:box_id>/delete/', views.delete_box, name='delete_box'),
    path('box/<int:box_id>/note/create/', views.create_note, name='create_note'),
    path('note/<int:note_id>/', views.view_note, name='view_note'),
    path('note/<int:note_id>/edit/', views.edit_note, name='edit_note'),
    path('note/<int:note_id>/delete/', views.delete_note, name='delete_note'),
]
