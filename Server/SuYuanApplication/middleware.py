from .models import APIRequest


class APIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        #  记录接口请求信息
        if "/api/" in request.path:
            APIRequest.objects.create(path=request.path)

        return response
