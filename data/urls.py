from django.urls import path

from . import views

app_name = 'data'

urlpatterns = [
    path('', views.data, name='data'),
    # path('success/', views.output, name='success')
]