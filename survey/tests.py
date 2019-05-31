import pytest
from survey.models import *
from django.test import TestCase


class QuestionTest(TestCase):
    def setUp(self):
        self.question_text = "Question text?"

        self.test_question = Question.objects.create(
            question_text=self.question_text,
        )

    def test_create_question(self):
        assert isinstance(self.test_question, Question)


class ChoiceTest(TestCase):
    def setUp(self):
        self.choice_text = "Choice value"
        self.question_text = "Question text?"
        self.correct_answer = False
        self.question = Question.objects.create(
            question_text=self.question_text,
        )

        self.test_choice = Choice.objects.create(
            choice_text=self.choice_text,
            correct_answer=self.correct_answer,
            question=self.question
        )

    def test_create_choice(self):
        assert isinstance(self.test_choice, Choice)


class UserResponseTest(TestCase):
    def setUp(self):
        self.choice_text = "Choice value"
        self.question_text = "Question text?"
        self.correct_answer = False

        self.user = User.objects.create_user(
                    username='test',
                    email='test@marcos.com',
                    password='test@123456')

        self.question = Question.objects.create(
            question_text=self.question_text,
        )

        self.choice = Choice.objects.create(
            choice_text=self.choice_text,
            correct_answer=self.correct_answer,
            question=self.question
        )

        self.test_userresponse = UserResponse.objects.create(
            user=self.user,
            choice=self.choice,
            question=self.question,
            iscorrect=False
        )

    def test_create_userresponse(self):
        assert isinstance(self.test_userresponse, UserResponse)
