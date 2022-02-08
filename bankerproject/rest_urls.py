from django.urls import path, include
from rest_framework import routers

from banker import rest_views as banker_rest_views

router = routers.DefaultRouter()
router.register(r'users', banker_rest_views.UserViewSet)
router.register(r'groups', banker_rest_views.GroupViewSet)
router.register(r'user-accounts', banker_rest_views.UserAccountViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
