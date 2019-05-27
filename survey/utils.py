import random
from survey.models import Choice, Question, UserResponse


def get_random_question(user, previous_question = ''):
    # Getting all responses for current user
    user_responses = UserResponse.objects.filter(user__id=user.id)
    
    # Extracting responses ids
    answered_ids = set(response.question.id for response in user_responses)
    
    #Filtering questions
    questions = Question.objects.exclude(id__in=answered_ids).order_by('?')[:1]
    
    if not questions:
        return None
    
    return random.choice(questions)

