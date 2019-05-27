from django.contrib import admin
from survey.models import Question, Choice, UserResponse

class QuestionInline(admin.StackedInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'choice', 'iscorrect',]
    readonly_fields = ['iscorrect',]

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResponse, UserResponseAdmin)
