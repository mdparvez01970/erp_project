from rest_framework import viewsets, permissions, filters, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, AccountHead, GeneralLedger
from .serializers import UserSerializer, AccountHeadSerializer, GeneralLedgerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from django.db.models import Sum
from rest_framework.decorators import action
from .utils import get_account_report

# Sign Up
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "success": True,
            "message": "User registered successfully",
            "user": {
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }, status=status.HTTP_201_CREATED)
        
# Sign Out
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"success": False, "error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"success": True, "message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AccountReportAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        report = get_account_report()
        return Response(report)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['username', 'email', 'role']
    ordering_fields = ['id', 'username', 'date_joined']
    filterset_fields = ['role', 'is_active']
    

class AccountHeadViewSet(viewsets.ModelViewSet):
    queryset = AccountHead.objects.all()
    serializer_class = AccountHeadSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'code']
    ordering_fields = ['id', 'code', 'name']
    filterset_fields = ['type']
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def report(self, request):
        accounts = AccountHead.objects.prefetch_related('generalledger_set').all()
        report_data = []
        for account in accounts:
            total_debit = account.generalledger_set.aggregate(total=Sum('debit'))['total'] or 0
            total_credit = account.generalledger_set.aggregate(total=Sum('credit'))['total'] or 0
            report_data.append({
                'account_code': account.code,
                'account_name': account.name,
                'account_type': account.type,
                'total_debit': total_debit,
                'total_credit': total_credit
            })
        return Response(report_data)


class GeneralLedgerViewSet(viewsets.ModelViewSet):
    queryset = GeneralLedger.objects.all().order_by("-date")
    serializer_class = GeneralLedgerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['description', 'account__name']
    ordering_fields = ['id', 'date', 'debit', 'credit']
    filterset_fields = ['date', 'account', 'account__type']
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
            
    @action(detail=False, methods=['get'])
    def report(self, request):
        accounts = AccountHead.objects.prefetch_related('generalledger_set').all()
        report_data = []

        for account in accounts:
            total_debit = account.generalledger_set.aggregate(total=Sum('debit'))['total'] or 0
            total_credit = account.generalledger_set.aggregate(total=Sum('credit'))['total'] or 0
            report_data.append({
                'account_code': account.code,
                'account_name': account.name,
                'account_type': account.type,
                'total_debit': total_debit,
                'total_credit': total_credit
            })

        return Response(report_data)
