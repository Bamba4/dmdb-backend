from django.contrib import admin
from .models import Employee, Audit, GodParent, Tutor, Student

admin.site.register(Employee)
admin.site.register(Audit)
admin.site.register(GodParent)
admin.site.register(Tutor)
admin.site.register(Student)
