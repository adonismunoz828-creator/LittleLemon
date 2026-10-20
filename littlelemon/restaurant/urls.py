from django.urls import path
from .views import MenuAPIView, SingleMenuItemView, index
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', index, name='index'),
    path('menu/items', MenuAPIView.as_view(), name='menu-items'),
    path('menu/items/', MenuAPIView.as_view(), name='menu-items-slash'),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('menu/items/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item-slash'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
