from django.urls import path
from . import views

app_name = 'tasks'  # This should be the same as the app_name defined in the main urls.py

urlpatterns = [
    path('', views.lists, name='lists'),
    path('create_list', views.create_list, name='create_list'),
    path('lists/<int:list_id>/', views.get_list, name='get_list'),
    path('lists/<int:list_id>/create_task', views.create_task, name='create_task'),
    path('lists/<int:list_id>/search', views.search_tasks, name='search_task'),
    path('lists/<int:list_id>/complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('lists/<int:list_id>/update/<int:task_id>/', views.update_task, name='update_task'),
    path('lists/<int:list_id>/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
