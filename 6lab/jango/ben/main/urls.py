from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('info', views.info, name='info'),
    path('add', views.add, name='add'),
    path('update/<int:pk>', views.redact.as_view(), name='redact'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
