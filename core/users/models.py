from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """ User Model
    *Description*
        Primary user model

        is_superuser: field is for root use
    """
    email = models.EmailField(_('email address'), blank=False, unique=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = _("Users")
        
