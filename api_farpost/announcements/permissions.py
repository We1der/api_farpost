from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrAdminOrReadOnly(BasePermission):
    """ Пермишин для ограничения доступа не авторизованным и не
     являющимся авторами пользователям """
    def has_permission(self, request, view):
        is_method_safe = request.method in SAFE_METHODS

        return is_method_safe or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        is_method_safe = request.method in SAFE_METHODS
        is_user_author = obj.author == request.user

        return (is_method_safe or is_user_author
                or request.user.is_superuser or request.user.is_staff)
