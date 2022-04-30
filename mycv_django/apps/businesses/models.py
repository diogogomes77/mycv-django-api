from django.db import models


class Country(models.Model):
    class Meta:
        verbose_name_plural = "countries"

    country = models.CharField(max_length=32)

    def __str__(self):
        return self.country


class Business(models.Model):

    class Meta:
        verbose_name_plural = "businesses"

    name = models.CharField(max_length=64, blank=False)
    country = models.ForeignKey("businesses.Country", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
