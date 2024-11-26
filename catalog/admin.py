from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Library, Language

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Library)

# Define the admin class


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id','library')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

