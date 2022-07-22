from django.contrib import admin
from django.urls import path
from article import views

urlpatterns = [
    path('article/<int:id>', views.details, name='article_details'),
    path('article/<int:id>/edit', views.edit, name='article_edit'),
    path('article/<int:id>/delete', views.delete, name='article_delete'),
    path('article/create/', views.create, name='article_create'),
    path('article/', views.index, name='article_index'),
    path('admin/', admin.site.urls),
]
