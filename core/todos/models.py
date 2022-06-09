from django.db import models

from django.utils.translation import ugettext_lazy as _


class Todo(models.Model):
    """ Todo Model
    *Description*
        Holds data for the todos.
    """

    STATUSES = (("Completed", "Completed"), ("In Progress", "In Progress"), ("Active", "Active"),)

    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default="Active",
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=False,
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
