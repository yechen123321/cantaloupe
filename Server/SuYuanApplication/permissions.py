from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    # 判断对使用此权限类的视图是否有访问权限
    def has_permission(self, request, view):
        # 任何用户对使用此权限类的视图都没有访问权限
        if request.user:
            print(request.user.is_staff)
            return True
        return False
