from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
import json


class Question(models.Model):
    """ Model that holds questions records

    Returns:
        String  -- question text value
    """
    question_text = models.CharField(max_length=200, verbose_name=u"Question")

    def __str__(self):
        return '%s' % (self.question_text)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    @property
    def total_correct(self):
        return self.userresponse_set.filter(iscorrect=True).count()

    @property
    def total_incorrect(self):
        return self.userresponse_set.filter(iscorrect=False).count()


class Choice(models.Model):
    """ Model that holds the choices for each question

    Returns:
        string -- choice text value
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20, verbose_name=u"Choice")
    correct_answer = models.BooleanField(
                            default=False,
                            verbose_name="Select correct answer")

    def __str__(self):
        return '%s' % (self.choice_text)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"


class UserResponse(models.Model):
    """ Model that holds the responses
        or relationships between users,
        and choices selected

    Returns:
        string -- question and choice answered
    """
    user = models.ForeignKey(
                        User, null=True, blank=True,
                        on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    iscorrect = models.BooleanField(default=False)

    def __str__(self):
        return '%s  -  %s' % (self.question, self.choice)

    class Meta:
        verbose_name = "User Response"
        verbose_name_plural = "User  Responses"

    def save(self, *args, **kwargs):
        self.iscorrect = True if self.choice.correct_answer is True else False
        super(UserResponse, self).save(*args, **kwargs)

    @property
    def question_text(self):
        return self.question.question_text

    @property
    def choice_text(self):
        return self.choice.choice_text

    @property
    def username(self):
        return self.user.username if (self.username) else '-'
