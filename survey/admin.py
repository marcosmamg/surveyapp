from django.contrib import admin
from survey.models import Question, Choice, UserResponse

class QuestionInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResponse)
