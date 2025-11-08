from django.shortcuts import render
from .models import Question
# Create your views here.
def home(request):
    questions = Question.objects.all()
    return render(request, 'quiz/home.html')
