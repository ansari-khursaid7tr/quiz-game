from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('question/<int:number>/', views.get_question, name='get_question'),
    path('reveal_answer/<int:question_id>/', views.reveal_answer, name='reveal_answer'),
    path('reset_questions/', views.reset_questions, name='reset_questions'),
    #path(''),
]
