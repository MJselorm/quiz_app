from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question

# Create your views here.
def home(request):
    return render(request, 'quiz/home.html')


def start_quiz(request):
    # Get all quizzes
    quizzes = Quiz.objects.all()
    quiz_data = []
    
    for quiz in quizzes:
        count = quiz.questions.count()
        if count > 0:  # Only show quizzes that have questions
            quiz_data.append({
                'id': quiz.id,
                'name': quiz.name,
                'description': quiz.description,
                'quiz_type': quiz.quiz_type,
                'slug': quiz.slug,
                'count': count
            })
    
    return render(request, 'quiz/start-quiz.html', {'quiz_data': quiz_data})


def quiz_detail(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    questions = quiz.questions.all()
    
    return render(request, 'quiz/quiz-detail.html', {
        'quiz': quiz,
        'questions': questions
    })