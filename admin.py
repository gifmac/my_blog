

# Register your models here.

from django.contrib import admin

# Register your models here.
# to add, delete, and edit models, we must add admin.
# # also have to import the post

from .models import Post, Author

# we want to make the model visible in the admin page.
admin.site.register(Post)
admin.site.register(Author)
