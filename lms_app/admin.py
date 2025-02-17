from django.contrib import admin
from .models import Author, book, member, loan

# Register your models here.
class authorAdmin(admin.ModelAdmin):
    list_display=['author_id', 'author']

class bookAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'publisher_id', 'author_id']

class memberAdmin(admin.ModelAdmin):
    list_display=['member_id', 'member_first_name', 'member_last_name', 'membership_date']

class loanAdmin(admin.ModelAdmin):
    list_display=['loan_id', 'member_id', 'book_id', 'return_date']

admin.site.register(Author,authorAdmin)
admin.site.register(book,bookAdmin)
admin.site.register(member,memberAdmin)
admin.site.register(loan,loanAdmin)