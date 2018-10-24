from api.get_image_set import GetImageSetHandler

routes = {
    'get_image_set': GetImageSetHandler
}

def route(endpoint):
    handler = routes[endpoint]
    return handler()._process()