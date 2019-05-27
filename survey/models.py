from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField( max_length=200, verbose_name=u"Question")

    def __str__(self):
        return '%s' % (self.question_text)        

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20, verbose_name=u"Choice")
    correct_answer =  models.BooleanField(default = False,verbose_name="Select correct answer")

    def __str__(self):
        return '%s' % (self.choice_text)        

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {}'.format(self.user, self.question, self.choice)
    
    class Meta:
        verbose_name = "User Response"
        verbose_name_plural = "User  Responses"

