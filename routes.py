from api.get_image_set import GetImageSetHandler

routes = {
    'get_image_set': GetImageSetHandler()
}

def route(endpoint):
    return routes[endpoint]