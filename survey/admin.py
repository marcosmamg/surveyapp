from django.contrib import admin
from survey.models import Question, Choice, UserResponse


class QuestionInline(admin.StackedInline):
    """[summary]

    Arguments:
        admin {[type]} -- [description]
    """
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    """[summary]

    Arguments:
        admin {[type]} -- [description]
    """
    inlines = [
        QuestionInline,
    ]


class UserResponseAdmin(admin.ModelAdmin):
    """[summary]

    Arguments:
        admin {[type]} -- [description]
    """
    list_display = ['user', 'question', 'choice', 'iscorrect', ]
    readonly_fields = ['iscorrect', ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResponse, UserResponseAdmin)
