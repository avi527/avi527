from django.db import models

# Create your models here.
class Libraries(models.Model):
    libraries_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Books(models.Model):
    book_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    isbn_num = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    discription = models.TextField()
    def __str__(self):
        return self.title


class Library_books(models.Model):
    library_book_id = models.AutoField(primary_key = True)
    library_id = models.ForeignKey(Libraries,on_delete=models.CASCADE,related_name="Libraries",default=None)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE,related_name="Books",default=None)
    last_library_activity_id = models.IntegerField()

class Users(models.Model):
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Library_activites(models.Model):
    act_types = (
    ("out", "Out"),
    ("in", "In"))
    library_activity_id = models.AutoField(primary_key = True)
    activity_type = models.CharField(choices=act_types,max_length=10)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    library_book_id = models.ForeignKey(Library_books,on_delete=models.CASCADE, default=None)
    # checked_out_at = models.TextField(auto_now_add=False,auto_now=False,blank=True)
    checked_out_at = models.TextField(max_length=20,default="0000-00-00")
    checked_in_at = models.TextField(max_length=20,default="0000-00-00")
