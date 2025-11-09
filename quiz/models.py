from django.db import models

# Create your models here.
class Question(models.Model):
    QUIZ_TYPES = [
        ('MATH', 'Math'),
        ('SCI', 'Science'),
        ('HIST', 'History'),
    ]
    
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
    quiz_type = models.CharField(
        max_length=10,
        choices=QUIZ_TYPES,
        default='MATH'
    )
    
    def __str__(self):
        return self.question_text