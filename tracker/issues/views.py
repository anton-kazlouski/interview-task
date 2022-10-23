from rest_framework.viewsets import ModelViewSet

from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
	queryset = Issue.objects.all()
	serializer_class = IssueSerializer
