from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AccountHeadViewSet, GeneralLedgerViewSet, RegisterView, LogoutView, AccountReportAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountHeadViewSet)
router.register(r'GeneralLedger', GeneralLedgerViewSet)

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('report/', AccountReportAPIView.as_view(), name='account-report'),
    
    path('', include(router.urls)),
]
