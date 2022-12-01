from XplrBg.core.utils.errors import error404, error400, error403


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 400:
            return error400(request)
        if response.status_code == 403:
            return error403(request)
        if response.status_code == 404:
            return error404(request)
        # elif response.status_code >= 500:
        #     return internal_server_error(request)
        return response

    return middleware