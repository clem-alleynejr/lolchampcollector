from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lolchamps/', views.lolchamps_index, name='lolchamps'),
    path('about/', views.about, name='about'),
    path('lolchamps/<int:lolchamp_id>/', views.lolchamp_details, name='details'),
    path('lolchamps/create/', views.LolChampCreate.as_view(), name='lolchamps_create'),
    path('lolchamps/<int:pk>/update/', views.LolChampUpdate.as_view(), name='lolchamps_update'),
    path('lolchamps/<int:pk>/delete/', views.LolChampDelete.as_view(), name='lolchamps_delete'),
    path('lolchamps/<int:lolchamp_id>/add_ability/', views.add_ability, name='add_ability'),
    path('lolchamps/<int:lolchamp_id>/assoc_item/<int:item_id>/', views.assoc_item, name='assoc_item'),
    path('items/', views.ItemList.as_view(), name='items_index'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='items_detail'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]