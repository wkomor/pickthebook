from django.contrib import admin

from .models import Book, Question, Author, QuestionType, Ancestor, Descendant
# Register your models here.




class AncInline(admin.TabularInline):
    model = Ancestor
    fk_name = 'ancestor'
    extra = 1


class DescInline(admin.TabularInline):
    model = Descendant
    fk_name = 'descendant'
    extra = 2



class QuestionAdmin(admin.ModelAdmin):
    inlines = [AncInline, DescInline]
    list_display = ('q_text',)





admin.site.register(Book)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Author)
admin.site.register(QuestionType)
