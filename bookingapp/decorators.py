from django.core.exceptions import PermissionDenied


def user_is_owner(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == "owner":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_visitor(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == "visitor":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
