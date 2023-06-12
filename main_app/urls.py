from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lolchamps/', views.lolchamps_index, name='lolchamps'),
    path('about/', views.about, name='about'),
    path('lolchamps/<int:lolchamp_id>/', views.lolchamp_details, name='details')
]