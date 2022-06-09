from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TodoConfig(AppConfig):
    name = "core.todos"
    verbose_name = _("Todos")
