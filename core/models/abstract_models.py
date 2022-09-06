from django.db import models 


class Coordinates(models.Model):
    """
    Model to be inherited into other models that needs to receive addresses and coordinates.

    :param models (module): hold fields and params to be used into models.
    """
    address = models.CharField(max_length=512, blank=True)
    neighborhood = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    state = models.CharField(max_length=120, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=30, blank=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)

    class Meta:
        abstract = True