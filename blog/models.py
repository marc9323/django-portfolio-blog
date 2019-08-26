from django.db import models

# Create your models here.
#title
#publication date
#body
#image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# blog model create

# add blog app to the settings

# create a migration

# migrate

# add to the admin
