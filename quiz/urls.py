
from django.urls import path
from . import views

app_name='quiz'

urlpatterns = [
    path('',views.home, name='home'),
    path('start-quiz/', views.start_quiz, name='start-quiz'),
]
