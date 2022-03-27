from django.db import models

# Create your models here.
class Profile(models.Model):
    x = [
        ('VIP', 'VPIP'),
        ('Geust', 'Geust'),
        ('Owner', 'Owner'),
    ]
    name = models.CharField(max_length=50, verbose_name='NAME -_-')
    price = models.DecimalField(max_digits=6, decimal_places=2, default="44.44")
    content = models.TextField(default="bla bla bla", blank=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    active = models.BooleanField(default=True, null=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # sordering
        verbose_name = 'ahmed'
