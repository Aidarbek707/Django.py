from django.contrib import admin
from .models import Employees
from .models import Question, Choice

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name','position','salary')
    list_filter = ('position',)
    search_fields = ('name',)

admin.site.register(Employees,EmployeesAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question','choice_text', 'votes']



admin.site.register(Question)
admin.site.register(Choice,ChoiceAdmin)