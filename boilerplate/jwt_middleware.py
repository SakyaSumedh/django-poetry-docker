from re import compile as re_compile

from django.conf import settings
from django.http import JsonResponse
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.exceptions import InvalidToken

EXEMPT_URLS = [re_compile(expr) for expr in settings.LOGIN_EXEMPT_PATHS]


class JWTTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path_info.lstrip("/")
        if not JWTTokenMiddleware.is_exempt_url(path):
            try:
                request.user = authentication.JWTAuthentication().authenticate(request)[0]
            except InvalidToken:
                if "/logout" in path:
                    return JsonResponse({"detail": "Successfully logged out."}, status=200)

                return JsonResponse({"error": "Token is invalid or expired"}, status=401)
            except TypeError:
                return JsonResponse({"error": "Token is not provided"}, status=401)

        return view_func(request, *view_args, **view_kwargs)

    @classmethod
    def is_exempt_url(cls, path):
        if not any(url.match(path) for url in EXEMPT_URLS):
            return False
        return True
