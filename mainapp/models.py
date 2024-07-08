from django.db import models


class News(models.Model):
    """ User can upload thier email for the news later"""

    emails = models.EmailField(max_length=254)

    def __str__(self):
        return self.emails