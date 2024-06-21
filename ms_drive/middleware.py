from django.shortcuts import redirect

class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_staff and request.path == '/':
            return redirect('/admin/')
        response = self.get_response(request)
        return response

