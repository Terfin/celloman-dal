from django.db import models
from django.core import validators
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your models here.


class Client(User):
    type = models.ForeignKey('ClientType', null=True, related_name='clients')
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20, validators=[validators.RegexValidator('[\+]{0,1}[0-9][0-9\-]+')])
    calls_to_center = models.IntegerField()

class Line(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, help_text="The user of this phone line", null=True, blank=True)
    number = models.CharField(max_length=20)
    status = models.CharField(max_length=15)
    package = models.ForeignKey('Package')


class Call(models.Model):
    line = models.ForeignKey(Line)
    duration = models.FloatField()
    external_price = models.FloatField()
    destination_number = models.CharField(max_length=20, validators=[validators.RegexValidator('[\+]{0,1}[0-9][0-9\-]+')])


class ClientType(models.Model):
    name = models.CharField(max_length=100)
    minutes_price = models.FloatField()
    sms_price = models.FloatField()


class Package(models.Model):
    name = models.CharField(max_length=100)
    total_price = models.FloatField()


class PackageInclude(models.Model):
    name = models.CharField(max_length=100)
    max_minute = models.IntegerField()
    fixed_price = models.FloatField()
    discount_percentage = models.FloatField()
    selected_numbers = models.ForeignKey('SelectedNumbers', null=True)
    most_called_number = models.BooleanField(default=False)
    inside_family_calls = models.BooleanField(default=False)


class SelectedNumbers(models.Model):
    first_number = models.CharField(max_length=20, validators=[validators.RegexValidator('[\+]{0,1}[0-9][0-9\-]+')])
    second_number = models.CharField(max_length=20, validators=[validators.RegexValidator('[\+]{0,1}[0-9][0-9\-]+')])
    third_number = models.CharField(max_length=20, validators=[validators.RegexValidator('[\+]{0,1}[0-9][0-9\-]+')])


class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_date = models.DateField()
    total_payment = models.FloatField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:
            self.payment_date = timezone.now().date()
        super().save(force_insert, force_update, using, update_fields)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)