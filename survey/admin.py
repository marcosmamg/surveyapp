from django.contrib import admin
from survey.models import Question, Choice, UserResponse
from jet.admin import CompactInline

class QuestionInline(CompactInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResponse)
