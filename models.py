from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Author(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    photo = models.ImageField(blank=True, null=True)  # blank and null True leaves the field blank, in case
    #  we  dcreateo not image for all image fields
    #  creates a string representation of the class Author

    def __str__(self):
        return "My name is {}, {}, email: {}".format(self.first_name, self.last_name, self.email)

# defines our model post, models.Model means the Post is a django Model, so django knows to save it in db


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    # author = models.ForeignKey(Author,on_delete=models.CASCADE) # each post is associated with an author in Author class
    #  ForeignKey means there is a link to another model or class
    #  When an object referenced by a ForeignKey is deleted, Django will emulate the behavior of the SQL
    #  constraint specified by the on_delete argument.
    # the models.CASCADE tells django that when the Foreign key is deleted to delete all instance of Post
    #  that depend on it

    title = models.CharField(max_length= 200) # defines a text with a limited numbers of characters
    text = models.TextField()                 #  defines a text without a limit
    created_date = models.DateTimeField(default= timezone.now) # this is a date and time
    published_date = models.DateTimeField(blank=True, null=True)
    is_favored =  models.BooleanField(default=False)   # Boolean data type that adds a check mark

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def publish_recently(self):
        now = timezone.now()
        if self.published_date >= now - datetime.timedelta(days=10) or self.published_date == now:
                return ("This is a recent post, less than 10 day old")
        else:
                return ("this is an older post")


    def __str__(self):
            return("The post title is %s and it a %s post" %(self.title, self.published_date))


