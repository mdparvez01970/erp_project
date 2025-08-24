from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AccountHeadViewSet, GeneralLedgerViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountHeadViewSet)
router.register(r'GeneralLedger', GeneralLedgerViewSet)

urlpatterns = [
    path('jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
