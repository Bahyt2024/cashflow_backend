from django.urls import path
from . import views

urlpatterns = [
    # CRUD для движений денежных средств (ДДС)
    path('', views.CashFlowListView.as_view(), name='cashflow_list'),
    path('create/', views.CashFlowCreateView.as_view(), name='cashflow_create'),
    path('edit/<int:pk>/', views.CashFlowUpdateView.as_view(), name='cashflow_edit'),
    path('delete/<int:pk>/', views.CashFlowDeleteView.as_view(), name='cashflow_delete'),

    # CRUD для типов
    path('types/', views.TypeListView.as_view(), name='type_list'),
    path('types/create/', views.TypeCreateView.as_view(), name='type_create'),
    path('types/edit/<int:pk>/', views.TypeUpdateView.as_view(), name='type_edit'),
    path('types/delete/<int:pk>/', views.TypeDeleteView.as_view(), name='type_delete'),

    # CRUD для статусов
    path('statuses/', views.StatusListView.as_view(), name='status_list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('statuses/edit/<int:pk>/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('statuses/delete/<int:pk>/', views.StatusDeleteView.as_view(), name='status_delete'),

    # CRUD для категорий
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/edit/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # CRUD для подкатегорий
    path('subcategories/', views.SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategories/create/', views.SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategories/edit/<int:pk>/', views.SubCategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategories/delete/<int:pk>/', views.SubCategoryDeleteView.as_view(), name='subcategory_delete'),

    # API для динамического фильтра (категории по типу, подкатегории по категории)
    path('api/categories/<int:type_id>/', views.get_categories_by_type, name='api_categories_by_type'),
    path('api/subcategories/<int:category_id>/', views.get_subcategories_by_category, name='api_subcategories_by_category'),
]
