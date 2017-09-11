from django.contrib import admin
from .models import Question, Choice

# filtering data

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date')
	list_filter = ('question_text', 'question_text')
	search_fields = ('question_text', 'question_text')

admin.site.register(Question, QuestionAdmin)

# data filter

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('choice_text', 'votes')
	list_filter = ('votes', 'choice_text')
	search_fields = ('choice_text', 'choice_text')

admin.site.register(Choice, ChoiceAdmin)
