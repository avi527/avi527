from django.contrib import admin
from .models import Libraries,Books,Library_books,Users,Library_activites
# Register your models here.

admin.site.register(Libraries)
admin.site.register(Books)
admin.site.register(Library_books)
admin.site.register(Users)
admin.site.register(Library_activites)

