from rest_framework import permissions



class IsExamAuthor(permissions.BasePermission):
# this is a custom permission to reatrict access to Update and Delete another users exam
    message = "User is not the Author of this exam"
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsQuestionAuthor(permissions.BasePermission):
# this is a custom permission to reatrict access to Update and Delete another users exam

    message = "User is not the Author of this question"

    def has_object_permission(self, request, view, obj):
        return obj.exam.user == request.user