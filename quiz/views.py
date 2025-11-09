from django.shortcuts import render
from .models import Question
from django.db.models import Count

# Create your views here.
def home(request):
    return render(request, 'quiz/home.html')


def start_quiz(request):
    # Group questions by quiz type and count them
    quiz_types = Question.QUIZ_TYPES
    quiz_data = []
    
    for quiz_type, quiz_name in quiz_types:
        count = Question.objects.filter(quiz_type=quiz_type).count()
        if count > 0:  # Only show quiz types that have questions
            quiz_data.append({
                'type': quiz_type,
                'name': quiz_name,
                'count': count
            })
    
    return render(request, 'quiz/start-quiz.html', {'quiz_data': quiz_data})