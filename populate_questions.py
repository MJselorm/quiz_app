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
        description="Test your mathematical skills with this comprehensive quiz covering algebra, geometry, and calculus.",
        quiz_type="MATH"
    )
    
    science_quiz = Quiz.objects.create(
        name="Science Quiz",
        description="Explore the wonders of science including physics, chemistry, and biology.",
        quiz_type="SCI"
    )
    
    history_quiz = Quiz.objects.create(
        name="History Quiz",
        description="Journey through historical events from ancient civilizations to modern times.",
        quiz_type="HIST"
    )
    
    tech_quiz = Quiz.objects.create(
        name="Technology Quiz",
        description="Test your knowledge of computers, programming, and modern technology.",
        quiz_type="TECH"
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
        },
        {
            'question_text': 'What is the square root of 144?',
            'option_a': '10',
            'option_b': '12',
            'option_c': '14',
            'option_d': '16',
            'correct_option': 'B',
            'quiz': math_quiz
        },
        {
            'question_text': 'What is 15% of 200?',
            'option_a': '25',
            'option_b': '30',
            'option_c': '35',
            'option_d': '40',
            'correct_option': 'B',
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
        },
        {
            'question_text': 'What is the powerhouse of the cell?',
            'option_a': 'Nucleus',
            'option_b': 'Mitochondria',
            'option_c': 'Ribosome',
            'option_d': 'Endoplasmic Reticulum',
            'correct_option': 'B',
            'quiz': science_quiz
        },
        {
            'question_text': 'What is the speed of light in vacuum?',
            'option_a': '300,000 km/s',
            'option_b': '150,000 km/s',
            'option_c': '450,000 km/s',
            'option_d': '600,000 km/s',
            'correct_option': 'A',
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
        },
        {
            'question_text': 'Who was the first President of the United States?',
            'option_a': 'Thomas Jefferson',
            'option_b': 'John Adams',
            'option_c': 'George Washington',
            'option_d': 'Benjamin Franklin',
            'correct_option': 'C',
            'quiz': history_quiz
        },
        {
            'question_text': 'Which ancient civilization built the pyramids?',
            'option_a': 'Romans',
            'option_b': 'Greeks',
            'option_c': 'Egyptians',
            'option_d': 'Mesopotamians',
            'correct_option': 'C',
            'quiz': history_quiz
        }
    ]
    
    # Create sample Technology questions
    tech_questions = [
        {
            'question_text': 'What does CPU stand for?',
            'option_a': 'Central Processing Unit',
            'option_b': 'Computer Personal Unit',
            'option_c': 'Central Processor Unit',
            'option_d': 'Central Program Unit',
            'correct_option': 'A',
            'quiz': tech_quiz
        },
        {
            'question_text': 'Which programming language is known as the language of the web?',
            'option_a': 'Python',
            'option_b': 'Java',
            'option_c': 'JavaScript',
            'option_d': 'C++',
            'correct_option': 'C',
            'quiz': tech_quiz
        },
        {
            'question_text': 'What is the main programming language used for Android development?',
            'option_a': 'Swift',
            'option_b': 'Kotlin',
            'option_c': 'Python',
            'option_d': 'Ruby',
            'correct_option': 'B',
            'quiz': tech_quiz
        }
    ]
    
    # Add all questions to database
    all_questions = math_questions + science_questions + history_questions + tech_questions
    
    for q_data in all_questions:
        question = Question.objects.create(**q_data)
        print(f"Created question: {question.question_text}")
    
    print(f"Total quizzes created: {Quiz.objects.count()}")
    print(f"Total questions created: {Question.objects.count()}")

if __name__ == '__main__':
    populate_questions()