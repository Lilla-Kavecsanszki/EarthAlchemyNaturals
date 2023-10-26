from django.db import models
from django.contrib.auth.models import User


class Membership(models.Model):
    """
    Represents the membership status.
    """

    MEMBERSHIP_STATUS_CHOICES = [
        ('Member', 'Member'),
        ('None', 'None'),
    ]

    # Membership status
    status = models.CharField(
        max_length=100,
        choices=MEMBERSHIP_STATUS_CHOICES,
        default='None',
    )
    # Foreign keyto the User model
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             related_name='membership', null=True, blank=True)
    # Information about the benefits of being a member
    description = models.TextField()
    # Price for the membership (annual fee)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    # Duration of the membership (1 year)
    duration_months = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.status)
