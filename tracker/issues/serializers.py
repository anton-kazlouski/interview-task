from rest_framework import serializers
from .models import Issue


class DynamicFieldsMixin:
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class IssueSerializer(
    serializers.ModelSerializer,
    DynamicFieldsMixin,
):
    class Meta:
        model = Issue
        fields = '__all__'
