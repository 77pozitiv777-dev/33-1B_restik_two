from django.db import models

class Settings(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'
