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

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# like toString() in Java, so admin page reflects 
# by title
    def __str__(self):
        return self.title



# blog model create

# add blog app to the settings

# create a migration

# migrate

# add to the admin
