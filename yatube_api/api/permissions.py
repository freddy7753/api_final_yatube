from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Проверка прав на изменение поста"""
    message = 'Do not right to change object'
    # Как вынести так, что бы тесты не падали пойду в пачку,
    # не получается чёт

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author)
