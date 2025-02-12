
class Abstract:
    def post_param(self, request, param):
        if param in request.POST:
            return request.POST.get(param)
        else:
            return None