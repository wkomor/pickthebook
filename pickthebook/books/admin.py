from django.contrib import admin

from .models import Book, Question, Author, Answer
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('q_text',)

admin.site.register(Book)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Author)
#admin.site.register(Answer)