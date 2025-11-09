from django.db import models
from django.utils.text import slugify

class Quiz(models.Model):
    QUIZ_TYPES = [
        ('MATH', 'Math'),
        ('SCI', 'Science'),
        ('HIST', 'History'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quiz_type = models.CharField(
        max_length=10,
        choices=QUIZ_TYPES,
        default='MATH'
    )
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.name)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
        help_text="Choose the correct option"
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    
    def __str__(self):
        return str(self.question_text)