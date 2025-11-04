from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Appeal
from .serializers import AppealSerializer

class AppealViewSet(viewsets.ModelViewSet):
    queryset = Appeal.objects.all().order_by('-created_at')
    serializer_class = AppealSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student__username', 'submission__assignment__title', 'reason', 'status']
    ordering_fields = ['created_at', 'status']
    ordering = ['-created_at']
