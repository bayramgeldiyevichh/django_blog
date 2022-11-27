from django.db import models

class Settings(models.Model):
    phone = models.CharField(max_length=120)
    email = models.EmailField()
    addres  = models.CharField(max_length=200)
    instagram = models.URLField(max_length=250)
    linkeding = models.URLField(max_length=250)
    facebook = models.URLField(max_length=250)

    class Meta:
        verbose_name = "Sazlamalar"
        verbose_name_plural = "Sazlamalar"

    def __str__(self):
        return self.phone

class Services(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='services')
    description = models.TextField()

    class Meta:
        verbose_name = "Hyzmatlarymyz"
        verbose_name_plural = "Hyzmatlarymyz"

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='about')
    description = models.TextField()

    class Meta:
        verbose_name = "Biz hakynda"
        verbose_name_plural = "Biz hakynda"

    def __str__(self):
        return self.title

class WorkOur(models.Model):
    title = models.CharField(max_length=120)
    title_addres = models.CharField(max_length=150)
    addres = models.URLField(max_length=200)

    class Meta:
        verbose_name = "Edilen işler"
        verbose_name_plural = "Edilen işelr"

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    email = models.EmailField(max_length=50, verbose_name="Email poçtasy")
    name = models.CharField(max_length=100, verbose_name="Ady")
    last_name = models.CharField(max_length=150, verbose_name="Familiyasy")
    phone = models.CharField(max_length=50, verbose_name="El telefony")
    message = models.TextField(verbose_name="SMS")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)


    class Meta:
        verbose_name = 'SMS'
        verbose_name_plural = 'SMSLER'

