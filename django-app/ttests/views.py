from rest_framework import generics
from .models import Test
from .serializers import TestSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from schools.permissions import IsAdminOrSchoolOwner
from rest_framework.permissions import IsAuthenticated
from classrooms.models import Classroom
from classes.models import Class
from courses.models import Course
from schools.models import School
from schools.mixins import SchoolPermissionMixin
from rest_framework.exceptions import NotFound


class TestView(SchoolPermissionMixin, generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrSchoolOwner]

    serializer_class = TestSerializer

    school_url_kwarg = 'school_id'

    def get_queryset(self):
        school_id = self.kwargs[self.school_url_kwarg]
        return Test.objects.filter(
            classroom__cclass__course__school_id=school_id,
        )

    def perform_create(self, serializer):

        school_id = self.kwargs[self.school_url_kwarg]
        classroom_id = self.request.data.get('classroom_id')

        find_school = School.objects.filter(pk=school_id).first()
        if not find_school:
            raise NotFound("School not found")

        find_classroom = Classroom.objects.filter(
            pk=classroom_id,
            cclass__course__school_id=school_id
        ).first()
        if not find_classroom:
            raise NotFound("Classroom not found")

        serializer.save(classroom_id=classroom_id,)


class TestDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrSchoolOwner,]

    queryset = Test.objects.all()
    serializer_class = TestSerializer

    lookup_url_kwarg = "test_id"
