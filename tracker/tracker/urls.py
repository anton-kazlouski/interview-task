from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from issues.views import IssueViewSet

router = SimpleRouter()

router.register('issues', IssueViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
