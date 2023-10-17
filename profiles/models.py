from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from membership.models import Membership

from django_countries.fields import CountryField


def get_non_member_status():
    return 1


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    membership_status = models.ForeignKey(
        Membership,
        on_delete=models.PROTECT,
        default=get_non_member_status,
        related_name='user_membership'
    )
    membership_start_date = models.DateTimeField(
        null=True, blank=True,
    )

    membership_duration = models.DurationField(
        null=True, blank=True,
    )

    def __str__(self):
        return self.user.username

@ receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        membership_instance, created = Membership.objects.get_or_create(
            status='None')
        if not isinstance(membership_instance, Membership):
            raise ValueError("Invalid Membership instance")
        UserProfile.objects.create(
            user=instance, 
            membership_status=membership_instance
        )
        # Existing users: just save the profile
    instance.userprofile.save()


class VIPBox(models.Model):

    class Meta:
        verbose_name_plural = 'VIP boxes'

    PACKAGING_COLOR_CHOICES = [
        ('pink', 'Pink Box'),
        ('gold', 'Gold Box'),
    ]

    selected_packaging_color = models.CharField(
        max_length=10,
        choices=PACKAGING_COLOR_CHOICES,
        default='pink',
    )

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"VIP Box ({self.selected_packaging_color})"
