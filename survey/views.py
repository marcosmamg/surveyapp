from django.shortcuts import render
from survey.models import Question, UserResponse, Choice, Question
from django import urls
from django.http import HttpResponseRedirect
from rest_framework import generics
from .serializers import UserResponseSerializer, QuestionSummarySerializer
import random


def get_random_question(session_key):
    """ Method returns a random question, excluding those that
        where responded already.

    Arguments:
        session_key char -- A unique seesion key to identify anonymous users

    Returns:
        Questions -- Non answered questions
    """
    # Getting all responses for current user
    user_responses = UserResponse.objects.filter(session_key=session_key)

    # Extracting responses ids
    answered_ids = set(response.question.id for response in user_responses)

    # Filtering questions
    questions = Question.objects.exclude(id__in=answered_ids).order_by('?')[:1]

    if not questions:
        return None

    return random.choice(questions)


def index(request):
    """ View for the index page,
        it renders the random question

    Arguments:
        request -- HttpRequest object that
        contains metadata about the request

    Returns:
        render -- returns a template with its context
    """
    question = get_random_question(request.session.session_key)
    context = {'question': question}
    if question is None:
        context['all_answered'] = Question.objects.all().count() > 0
    return render(request, 'survey/index.html', context)


def submission(request, question_id):
    """ View that validates choices and saves the response

    Arguments:
        request -- HttpRequest object that
        contains metadata about the request

        question_id int -- Question identifyer
        to relate response to user and choice

    Returns:
        HttpResponseRedirect -- Redirects the user to the index
    """
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'survey/index.html', {
            'question': question,
            'error_message': "Please select a choice.",
        })
    else:
        if (request.user.is_anonymous):
            if not request.session.session_key:
                request.session.save()

            UserResponse.objects.create(
                user=None,
                session_key=request.session.session_key,
                choice=selected_choice,
                question=question,
            )
        else:
            UserResponse.objects.create(
                user=request.user,
                session_key=request.session.session_key,
                choice=selected_choice,
                question=question,
            )

        redirect_url = urls.reverse('index')
        return HttpResponseRedirect(redirect_url)


def recreate_session(request):
    """ View that generates a new session to identify unique users

    Arguments:
        request -- HttpRequest object that
        contains metadata about the request

    Returns:
        HttpResponseRedirect -- Redirects the user to the index
    """
    request.session.flush()
    return HttpResponseRedirect(urls.reverse('index'))


class UserResponseList(generics.ListCreateAPIView):
    """ Class base view to create a readonly endpoint with DRF

    Arguments:
        generics -- Used for read-write endpoints to
        represent a collection of model instances.
    """
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer


class UserResponseSummaryList(generics.ListCreateAPIView):
    """ Class base view to create a readonly endpoint with DRF

    Arguments:
        generics -- Used for read-write endpoints to
        represent a collection of model instances.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSummarySerializer


def report(request):
    """ View used to render report

    Arguments:
        request -- HttpRequest object that
        contains metadata about the request

    Returns:
        HttpResponseRedirect -- Redirects the user to the index
    """
    context = {'user': 'Marcos Moreno'}
    return render(request, 'survey/report.html', context)
