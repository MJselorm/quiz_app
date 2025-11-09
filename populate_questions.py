import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Quiz, Question

def populate_questions():
    # Clear existing data
    Question.objects.all().delete()
    Quiz.objects.all().delete()
    
    # Create quizzes
    math_quiz = Quiz.objects.create(
        name="Mathematics Quiz",
        description="Test your mathematical skills",
        quiz_type="MATH"
    )
    
    science_quiz = Quiz.objects.create(
        name="Science Quiz",
        description="Explore the world of science",
        quiz_type="SCI"
    )
    
    history_quiz = Quiz.objects.create(
        name="History Quiz",
        description="Journey through historical events",
        quiz_type="HIST"
    )
    
    # Create sample Math questions
    math_questions = [
        {
            'question_text': 'What is 2 + 2?',
            'option_a': '3',
            'option_b': '4',
            'option_c': '5',
            'option_d': '6',
            'correct_option': 'B',
            'quiz': math_quiz
        },
        {
            'question_text': 'What is the value of π (pi) approximately?',
            'option_a': '3.14',
            'option_b': '2.71',
            'option_c': '1.61',
            'option_d': '4.67',
            'correct_option': 'A',
            'quiz': math_quiz
        }
    ]
    
    # Create sample Science questions
    science_questions = [
        {
            'question_text': 'What is the chemical symbol for water?',
            'option_a': 'H2O',
            'option_b': 'CO2',
            'option_c': 'NaCl',
            'option_d': 'O2',
            'correct_option': 'A',
            'quiz': science_quiz
        },
        {
            'question_text': 'What planet is known as the Red Planet?',
            'option_a': 'Venus',
            'option_b': 'Mars',
            'option_c': 'Jupiter',
            'option_d': 'Saturn',
            'correct_option': 'B',
            'quiz': science_quiz
        }
    ]
    
    # Create sample History questions
    history_questions = [
        {
            'question_text': 'In which year did World War II end?',
            'option_a': '1943',
            'option_b': '1945',
            'option_c': '1950',
            'option_d': '1939',
            'correct_option': 'B',
            'quiz': history_quiz
        }
    ]
    
    # Add all questions to database
    all_questions = math_questions + science_questions + history_questions
    
    for q_data in all_questions:
        question = Question.objects.create(**q_data)
        print(f"Created question: {question.question_text}")
    
    print(f"Total quizzes created: {Quiz.objects.count()}")
    print(f"Total questions created: {Question.objects.count()}")

if __name__ == '__main__':
    populate_questions()