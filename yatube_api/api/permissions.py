from rest_framework import permissions


class AuthorOrReadOnlyPermission(permissions.BasePermission):
    """Проверка прав на изменение поста"""
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author
