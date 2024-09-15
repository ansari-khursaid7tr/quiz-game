from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Question
from random import choice
from django.urls import reverse


def home(request):
    # Get selected numbers from the session
    selected_numbers = request.session.get('selected_numbers', [])

    context = {
        'numbers': range(1, 101),
        'selected_numbers': selected_numbers  # Pass selected numbers to the template
    }
    return render(request, 'quiz_app/home.html', context)


def get_question(request, number):
    unused_questions = Question.objects.filter(used=False)
    if unused_questions.exists():
        question = choice(unused_questions)
        question.used = True
        question.save()
    else:
        question = None

    # Add the clicked number to the selected_numbers list in session
    selected_numbers = request.session.get('selected_numbers', [])
    if number not in selected_numbers:
        selected_numbers.append(number)
        request.session['selected_numbers'] = selected_numbers  # Save back to session

    context = {
        'question': question,
        'number': number,
        'used_numbers': list(Question.objects.filter(used=True).values_list('id', flat=True))
    }
    return render(request, 'quiz_app/question.html', context)


def reveal_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return JsonResponse({'answer': question.answer})


def reset_questions(request):
    # Reset the database used flag and also clear the selected numbers in the session
    Question.objects.update(used=False)
    request.session['selected_numbers'] = []  # Clear session data for selected numbers
    return redirect('home')
