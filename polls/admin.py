from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
#TODO: To be added as part of admin module

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    #TODO: Diaplying more than just the question_text
    list_display = ("question_text","pub_date")

admin.site.register(Question, QuestionAdmin)

#TODO: 'Register' your modules into the admin page.
admin.site.register(Choice)