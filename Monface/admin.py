from django.contrib import admin
from Monface.models import Faculty, Student, Cursus, Job, Employee, Campus, Message, FriendRequest

# Register models without additional customization
admin.site.register(Faculty)
admin.site.register(Cursus)
admin.site.register(Job)
admin.site.register(Campus)
admin.site.register(Message)
admin.site.register(FriendRequest)
# Use @admin.register for models with customization
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('Amis',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    filter_horizontal = ('Amis',)
