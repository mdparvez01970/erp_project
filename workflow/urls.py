from rest_framework.routers import DefaultRouter
from .views import WorkflowViewSet, ApprovalViewSet

router = DefaultRouter()
router.register(r'workflows', WorkflowViewSet)
router.register(r'approvals', ApprovalViewSet)

urlpatterns = router.urls
