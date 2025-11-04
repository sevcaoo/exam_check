from rest_framework import serializers
from .models import Appeal, Student, Assignment, User  # kerakli modellar

class AppealSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.get_full_name', read_only=True)
    assignment_title = serializers.CharField(source='assignment.title', read_only=True)
    reviewed_by_name = serializers.CharField(source='reviewed_by.get_full_name', read_only=True)

    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    assignment = serializers.PrimaryKeyRelatedField(queryset=Assignment.objects.all())
    reviewed_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Appeal
        fields = [
            'id',
            'student_name',
            'student',
            'assignment',
            'assignment_title',
            'reason',
            'status',
            'reviewed_by',
            'reviewed_by_name',
            'review_notes',
            'reviewed_at',
            'created_at',
            'updated_at',
        ]
