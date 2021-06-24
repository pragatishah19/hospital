from django.contrib import admin
from .models import User,Books,Genre,Author

# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(User)