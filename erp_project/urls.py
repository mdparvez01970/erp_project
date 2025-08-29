"""
URL configuration for erp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts.views import RegisterView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Auth
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='signin'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Apps URLs
    path('api/accounts/', include('accounts.urls')),
    path('api/users/', include('users.urls')),
    path('api/assets/', include('assets.urls')),
    path('api/bank/', include('bank.urls')),
    path('api/budget/', include('budget.urls')),
    path('api/currency/', include('currency.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/expense/', include('expense.urls')),
    path('api/income/', include('income.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/payable/', include('payable.urls')),
    path('api/payroll/', include('payroll.urls')),
    path('api/receivable/', include('receivable.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/tax/', include('tax.urls')),
    path("api/files/", include("files.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/chat/", include("chat.urls")),
    path('api/workflow/', include('workflow.urls')),
    path('api/activity/', include('activity.urls')),


    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
