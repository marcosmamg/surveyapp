from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
import json
class Question(models.Model):
    question_text = models.CharField( max_length=200, verbose_name=u"Question")

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
    iscorrect = models.BooleanField(default = False)

    def __str__(self):
        return 'User: {}, was asked: {} Anwered: {} and the answer is: {}'.format(self.user, self.question, self.choice, self.iscorrect)
    
    class Meta:
        verbose_name = "User Response"
        verbose_name_plural = "User  Responses"

    def save(self, *args, **kwargs):
        self.iscorrect = True if self.choice.correct_answer == True else False
        super(UserResponse, self).save(*args, **kwargs)

    @property
    def question_text(self):
        return self.question.question_text

    @property
    def choice_text(self):
        return self.choice.choice_text

    @property
    def username(self):
        return self.user.username
        