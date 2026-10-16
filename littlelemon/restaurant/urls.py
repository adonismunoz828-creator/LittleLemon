from django.urls import path
from .views import MenuAPIView, SingleMenuItemView


urlpatterns = [
    path('menu/items', MenuAPIView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
]
