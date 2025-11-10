from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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
    
    if request.method == 'POST':
        # Process the quiz submission
        score = 0
        total = questions.count()
        user_answers = {}
        correct_answers = {}
        
        # Collect user answers and correct answers
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            user_answers[question.id] = user_answer
            correct_answers[question.id] = question.correct_option
            
            # Check if the answer is correct
            if user_answer == question.correct_option:
                score += 1
        
        # Calculate percentage
        percentage = (score / total) * 100 if total > 0 else 0
        
        # Determine remark based on score
        if percentage >= 80:
            remark = "Excellent! 🎉"
            remark_class = "excellent"
        elif percentage >= 60:
            remark = "Good Job! 👍"
            remark_class = "good"
        else:
            remark = "Keep Practicing! 💪"
            remark_class = "bad"
        
        # Prepare results data
        results = []
        for question in questions:
            results.append({
                'question_id': question.id,
                'question_text': question.question_text,
                'user_answer': user_answers.get(question.id),
                'correct_answer': correct_answers.get(question.id),
                'is_correct': user_answers.get(question.id) == correct_answers.get(question.id)
            })
        
        context = {
            'quiz': quiz,
            'questions': questions,
            'score': score,
            'total': total,
            'percentage': round(percentage, 1),
            'remark': remark,
            'remark_class': remark_class,
            'results': results,
            'show_results': True
        }
        
        return render(request, 'quiz/quiz-detail.html', context)
    
    return render(request, 'quiz/quiz-detail.html', {
        'quiz': quiz,
        'questions': questions
    })


def create_quiz(request):
    return render(request, 'quiz/create-quiz.html')