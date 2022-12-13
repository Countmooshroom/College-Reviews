from django.contrib import admin

from .models import Choice, Course, Teacher


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['course_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher)