from django.db import models
from django.contrib.auth.models import User


class HowMuchLike(models.Model):
    """The users leave their feedback"""

    class Meta:
        verbose_name_plural = 'Feedback'

    like = models.IntegerField(
        default=1, choices=(
            (i, i) for i in range(1, 11)
            ), null=False, blank=False
        )
    feedback = models.TextField(max_length=1000, null=True, blank=True)

    def __itin__(self):
        return self.like
