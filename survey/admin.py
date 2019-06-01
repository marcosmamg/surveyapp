from django.contrib import admin
from survey.models import Question, Choice, UserResponse


class QuestionInline(admin.StackedInline):
    """
        Representation of the choices
        model as an inline
    """
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    """
        Representation of the model
        in the admin for Questions
    """
    inlines = [
        QuestionInline,
    ]


class UserResponseAdmin(admin.ModelAdmin):
    """
        Representation of the model
        in the admin module for user responses
    """
    list_display = [
                    'user',
                    'session_key',
                    'question',
                    'choice',
                    'iscorrect',
                    ]
    readonly_fields = ['iscorrect', ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResponse, UserResponseAdmin)
