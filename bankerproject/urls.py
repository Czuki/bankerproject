from django.contrib import admin
from django.urls import path, include

from banker import views as banker_views

# router = routers.DefaultRouter()
# router.register(r'users', banker_views.UserViewSet)
# router.register(r'groups', banker_views.GroupViewSet)
# router.register(r'user-accounts', banker_views.UserAccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('bankerproject.rest_urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', banker_views.UserRegistrationView.as_view(), name='registration'),
    path('', banker_views.DashboardView.as_view(), name='dashboard')
]
