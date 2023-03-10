from rest_framework import serializers
from .models import Student, ClassRegistration, TestResult, Attendance
from utils.choice_messages import choices_error_message
from utils.choice_classes import GenderOptions


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'cpf',
            'gender',
            'birthdate',
            'phone',
            'email',
            'photo',
            "register_number",
            'is_active',
            'registered_at',
            'updated_at',
            'school_id',
        ]
        read_only_fields = ["register_number", 'registered_at', 'updated_at', 'fired_at', 'school_id']
        extra_kwargs = {
            "gender": {"error_messages": {"invalid_choice": choices_error_message(GenderOptions)}},
        }


class ClassRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassRegistration
        fields = [
            'id',
            'registered_at',
            'is_active',
            'student_id',
            'class_id',
        ]
        extra_kwargs = {"class_id": {"source": "cclass_id"}}


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = [
            'id',
            'test_grade',
            'student_id',
            'test_id',
        ]


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [
            'id',
            'showed_up',
            'register_date',
            'classroom_id',
            'student_id',
        ]
