from datetime import datetime, timedelta

from rest_framework import serializers
from .models import Issue

from django.core.mail import send_mail


class IssueSerializer(serializers.ModelSerializer):


	class Meta:
		model = Issue
		fields = '__all__'
