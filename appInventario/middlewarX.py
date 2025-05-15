from datetime import datetime
from django.http import HttpResponseForbidden

EXPIRATION_DATE = datetime(2025, 5, 18, 0, 0, 0) 

class ExpirationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if datetime.now() > EXPIRATION_DATE:
            return HttpResponseForbidden("Upps... Algo Falló. Comunicate con los creadores de la aplicación.")
        return self.get_response(request)