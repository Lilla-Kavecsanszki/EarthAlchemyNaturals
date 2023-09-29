from django.db import models


class Membership(models.Model):
    """
    Represents the membership status.
    """

    # membership status (e.g., "Member" or "Non-Member")
    status = models.CharField(max_length=100)

    # provide information about the benefits of being a member
    description = models.TextField()

    # Price for the membership (annual fee)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Duration of the membership (1 year)
    duration_months = models.PositiveIntegerField()

    def __str__(self):
        return self.name
