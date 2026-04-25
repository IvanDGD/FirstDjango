from django.http import HttpResponseNotFound
from django.urls import resolve, Resolver404
from django.shortcuts import redirect


class RedirectingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.sections = [
            "news",
            "management",
            "about",
            "contacts",
            "branches",
        ]

    def __call__(self, request):
        path = request.path.strip("/")

        try:
            resolve(request.path)

        except Resolver404:
            parts = path.split("/")

            if len(parts) >= 2:
                app_prefix = parts[0]
                section = parts[1]

                if section in self.sections:
                    return redirect(f"/{app_prefix}/{section}/")

            return HttpResponseNotFound("Page not found")

        return self.get_response(request)