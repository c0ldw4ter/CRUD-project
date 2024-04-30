from django.contrib import admin
from django.urls import path
from citys import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:city_id>/', views.delete, name='delete'),
    path('edit/<int:city_id>', views.edit, name='edit'),
]