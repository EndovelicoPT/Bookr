from django.contrib import admin
from reviews.models import (Publisher, Contributor, BookContributor, Book, \
                            Review)

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'isbn', 'get_publisher', 'publication_date')
    search_fields = ['title', 'publisher_name']

    def get_publisher(self, obj):
        return obj.publisher.name

class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited'),
    #fields = ('content', 'rating', 'creator', 'book')
    fieldsets = ((None, {'fields': ('creator', 'book')}),
                 ('Review content', {'fields': ('content', 'rating')}))

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names'),
    search_fields = ('last_names', 'first_names')


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)

