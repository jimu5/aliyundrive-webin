from . import app
from .views import search_file, get_download


def add_base_route(handler, uri, methods=['GET', 'OPTIONS'], **ctx_kwargs):
    uri = "/api" + uri
    if 'OPTIONS' not in methods:
        methods.append('OPTIONS')
    app.add_route(handler=handler, uri=uri, methods=methods, **ctx_kwargs)


add_base_route(search_file, "/search")
add_base_route(get_download, "/get_download")
