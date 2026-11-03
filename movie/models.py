from django.db import models

# Create your models here.
from django.db import models


class MovieQuestion(models.Model):
    OPTION_CHOICES = (
        ("A", "Option A"),
        ("B", "Option B"),
        ("C", "Option C"),
        ("D", "Option D"),
    )

    GENRE_CHOICES = (
        ("action", "Action"),
        ("comedy", "Comedy"),
        ("drama", "Drama"),
        ("sci_fi", "Sci-Fi"),
    )

    DIFFICULTY_CHOICES = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    )

    title = models.CharField(max_length=500)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(
        max_length=1,
        choices=OPTION_CHOICES
    )
    genre = models.CharField(
        max_length=20,
        choices=GENRE_CHOICES
    )
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )
    explanation = models.TextField()
    marks = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class MovieSubmission(models.Model):
    question_id = models.IntegerField()
    selected_option = models.CharField(max_length=1)
    is_correct = models.BooleanField(null=True, blank=True)
    points = models.PositiveIntegerField(null=True, blank=True)
    owner = models.CharField(max_length=100)
    remarks = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)