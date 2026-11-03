from rest_framework import serializers
from movie.models import MovieQuestion, MovieSubmission


class MovieQuestionSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=500)
    option_a = serializers.CharField(max_length=200)
    option_b = serializers.CharField(max_length=200)
    option_c = serializers.CharField(max_length=200)
    option_d = serializers.CharField(max_length=200)

    correct_option = serializers.ChoiceField(
        choices=MovieQuestion.OPTION_CHOICES
    )
    genre = serializers.ChoiceField(
        choices=MovieQuestion.GENRE_CHOICES
    )
    difficulty = serializers.ChoiceField(
        choices=MovieQuestion.DIFFICULTY_CHOICES
    )

    explanation = serializers.CharField()
    marks = serializers.IntegerField(min_value=1)
    is_active = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(read_only=True)


class MovieSubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_id = serializers.IntegerField()
    selected_option = serializers.ChoiceField(
        choices=MovieQuestion.OPTION_CHOICES
    )
    is_correct = serializers.BooleanField(
        read_only=True,
        allow_null=True
    )
    points = serializers.IntegerField(
        read_only=True,
        allow_null=True
    )
    owner = serializers.CharField(max_length=100)
    remarks = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )
    submitted_at = serializers.DateTimeField(read_only=True)

    def validate_question_id(self, value):
        if not MovieQuestion.objects.filter(
            id=value,
            is_active=True
        ).exists():
            raise serializers.ValidationError(
                "Active movie question does not exist."
            )

        return value