from django.shortcuts import render
from survey.models import Question, UserResponse, Choice, Question
from django import urls
from django.http import HttpResponseRedirect
from rest_framework import generics
from .serializers import UserResponseSerializer, QuestionSummarySerializer
import random

def get_random_question(user, previous_question=''):
    # Getting all responses for current user
    user_responses = UserResponse.objects.filter(user__id=user.id)

    # Extracting responses ids
    answered_ids = set(response.question.id for response in user_responses)

    # Filtering questions
    questions = Question.objects.exclude(id__in=answered_ids).order_by('?')[:1]

    if not questions:
        return None

    return random.choice(questions)


def index(request):
    question = get_random_question(request.user)
    context = {'question': question}
    if question is None:
        context['all_answered'] = Question.objects.all().count() > 0
    return render(request, 'survey/index.html', context)


def submission(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'survey/index.html', {
            'question': question,
            'error_message': "Please select a choice.",
        })
    else:
        UserResponse.objects.create(
            user=request.user,
            choice=selected_choice,
            question=question,
        )
        redirect_url = urls.reverse('index')
        return HttpResponseRedirect(redirect_url)


class UserResponseList(generics.ListCreateAPIView):
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer


class UserResponseSummaryList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSummarySerializer


def report(request):
    context = {'user': 'Marcos Moreno'}
    return render(request, 'survey/report.html', context)
