from django.core.exceptions import PermissionDenied

#Implementing the superuser_only method as a part of the decorator pattern
def superuser_only(function):
    def _inner(request, *args, **kwargs):
        #if the request is not from a super user, restrict access
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner
