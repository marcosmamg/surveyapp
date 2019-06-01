from rest_framework import serializers
from survey.models import UserResponse, Question


class UserResponseSerializer(serializers.ModelSerializer):
    """ Serializer to convert python data types to JSON
        or XML easily
    """
    username = serializers.ReadOnlyField()
    question_text = serializers.ReadOnlyField()
    choice_text = serializers.ReadOnlyField()
    iscorrect = serializers.ReadOnlyField()

    class Meta:
        model = UserResponse
        fields = (
                'id', 'username', 'question_text',
                'choice_text', 'iscorrect', )


class QuestionSummarySerializer(serializers.ModelSerializer):
    """ Serializer to convert python data types to JSON
        or XML easily
    """
    question_text = serializers.ReadOnlyField()
    total_correct = serializers.ReadOnlyField()
    total_incorrect = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'total_correct', 'total_incorrect')
