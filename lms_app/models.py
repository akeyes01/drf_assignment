from django.db import models

# Create your models here.
class author(models.Model):
    author_id = models.IntegerField(default=1)
    #id = models.IntegerField
    author = models.CharField(max_length=100)

class book(models.Model):
    book_id = models.IntegerField
    title = models.CharField(max_length=200)
    publisher_id = models.IntegerField(null=True)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    #author_id = models.ForeignKey(author, on_delete=models.CASCADE)

class member(models.Model):
    member_id = models.IntegerField(default=1)
    member_first_name = models.CharField(max_length=200)
    member_last_name = models.CharField(max_length=30)
    membership_date = models.DateField(null=True)

class loan(models.Model):
    loan_id = models.IntegerField(default=1)
    member_id = models.ForeignKey(member, on_delete=models.PROTECT)
    book_id = models.ForeignKey(book, on_delete=models.PROTECT)
    return_date = models.DateField(null=True)

