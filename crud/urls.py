from django.urls import path, re_path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    re_path(r'^edit/(?P<editing_id>\d+)/$', views.edit, name='edit'),
]
