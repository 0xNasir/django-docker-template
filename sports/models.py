from django.db import models
from django.template.defaultfilters import slugify


class Sport(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, True)
        super(Sport, self).save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=50, choices=(('preplay', 'preplay'), ('inplay', 'inplay')))
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=(
        ('Pending', 'Pending'), ('Started', 'Started'), ('Ended', 'Ended'), ('Cancelled', 'Cancelled')))
    scheduled_date = models.DateField()
    actual_start = models.DateField(blank=True)

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    outcome = models.CharField(max_length=50,
                               choices=(('Unsettled', 'Unsettled'), ('Void', 'Void'), ('Lose', 'Lose'), ('Win', 'Win')))

    def __str__(self):
        return self.name
