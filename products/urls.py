from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    path('list/', views.product_list, name='list'),
    path('create/', views.product_create, name='create'),
    path('detail/<int:detail_id>', views.product_detail, name='detail'),
    path('about/', views.about, name='about'),
]