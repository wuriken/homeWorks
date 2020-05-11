from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'first_name', 'last_name', 'age', 'education')
    readonly_fields = ('age', )


admin.site.register(Teacher, TeacherAdmin)
