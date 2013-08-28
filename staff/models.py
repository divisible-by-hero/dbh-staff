from django.db import models
from django.conf import settings

from .managers import StaffManager


class Staff(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)

    position = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)

    profile_picture = models.ImageField(upload_to="staff/images", blank=True, null=True)

    published = models.BooleanField(default=True)

    objects = StaffManager()

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"