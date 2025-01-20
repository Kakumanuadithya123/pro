from django.http import HttpResponseRedirect

class RewriteMiddleware:
    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        if not request.path.startswith('/assets/'):
            # Rewrite to /api/ssr.js
            request.path_info = '/api/ssr.js'
        return self.get_response(request)