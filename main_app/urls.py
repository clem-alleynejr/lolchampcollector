from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lolchamps/', views.lolchamps_index, name='lolchamps'),
    path('about/', views.about, name='about'),
    path('lolchamps/<int:lolchamp_id>/', views.lolchamp_details, name='details'),
    path('lolchamps/create/', views.LolChampCreate.as_view(), name='lolchamps_create'),
    path('lolchamps/<int:pk>/update/', views.LolChampUpdate.as_view(), name='lolchamps_update'),
    path('lolchamps/<int:pk>/delete/', views.LolChampDelete.as_view(), name='lolchamps_delete')
]