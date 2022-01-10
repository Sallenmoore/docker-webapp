from rest_framework import viewsets
from rest_framework import permissions
from api.models.course import Course
from api.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('-name')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
