from django.contrib import admin
from .models import Author, ProgramSupervisor, ProgramManager, ProgramInfo, Classmate

admin.site.register(Author)
admin.site.register(ProgramSupervisor)
admin.site.register(ProgramManager)
admin.site.register(ProgramInfo)
admin.site.register(Classmate)
