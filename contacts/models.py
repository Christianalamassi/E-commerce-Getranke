from django.db import models


class Question(models.Model):
    """Users send their request or question here"""

    name = models.CharField(max_length=45, blank=False, null=False )
    email = models.EmailField(max_length=75, blank=False, null=False )
    message = models.TextField(max_length=450, blank=False, null=False )

    def __str__(self):
        return self.name
