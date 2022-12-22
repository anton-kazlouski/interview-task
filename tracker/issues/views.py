from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(
                page,
                many=True,
                fields=('id', 'summary')
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(
            queryset,
            many=True,
            fields=('id', 'summary'),
        )
        return Response(serializer.data)
