from rest_framework import serializers
from survey.models import UserResponse


class UserResponseSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    question_text = serializers.ReadOnlyField()
    choice_text = serializers.ReadOnlyField()
    iscorrect = serializers.ReadOnlyField()

    class Meta:
        model = UserResponse
        fields = ('id', 'username', 'question_text', 'choice_text', 'iscorrect', )

class UserResponseSummarySerializer(serializers.ModelSerializer):
    question_text = serializers.ReadOnlyField()
    total_correct = serializers.ReadOnlyField()

    class Meta:
        model = UserResponse
        fields = ('id', 'question_text', 'total_correct', )