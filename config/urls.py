from django.conf import settings
from django.urls import include, path
from django.views import defaults as default_views

API_PREFIX = "v1"

#Routes
urlpatterns = [
    path(
        f"{API_PREFIX}/auth/",
        include(("core.auths.urls", "core.auths"), namespace="auth"),
    ),
    path(
        f"{API_PREFIX}/todos/",
        include(
            ("core.todos.urls", "core.todos"), namespace="todo"
        ),
    ),
    path(
        f"{API_PREFIX}/users/",
        include(
            ("core.users.urls", "core.users"), namespace="user"
        ),
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Sorry, looks like you don't have access to this action.")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

