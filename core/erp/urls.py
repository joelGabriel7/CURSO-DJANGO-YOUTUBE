from django.urls import path

from core.erp.views.category.views import *
from core.erp.views.dashboard.views import *

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),

    path('dashboard/', DashobardView.as_view(), name='dashboard')

]
