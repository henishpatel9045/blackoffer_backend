from django.db import models


# Create your models here.
class DataSource(models.Model):
    end_year = models.CharField(max_length=200, blank=True, null=True)
    intensity = models.IntegerField(blank=True, null=True)
    sector = models.TextField(max_length=200, blank=True, null=True)
    topic = models.TextField(max_length=2000, blank=True, null=True)
    insight = models.TextField(max_length=200, blank=True, null=True)
    url = models.TextField(max_length=2000, blank=True, null=True)
    region = models.TextField(max_length=200, blank=True, null=True)
    start_year = models.CharField(max_length=200, blank=True, null=True)
    impact = models.TextField(max_length=200, blank=True, null=True)
    added = models.CharField(max_length=200, blank=True, null=True)
    published = models.CharField(max_length=200, blank=True, null=True)
    country = models.TextField(max_length=500, blank=True, null=True)
    relevance = models.IntegerField(blank=True, null=True)
    pestle = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=2000, blank=True, null=True)
    likelihood = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
