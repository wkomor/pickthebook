from django.contrib import admin

from .models import Book, Question, Author, QuestionType
from mptt.admin import MPTTModelAdmin
# Register your models here.

class QuestionAdmin(MPTTModelAdmin):
    mptt_indent_field = "q_text"


admin.site.register(Book)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Author)
admin.site.register(QuestionType)
