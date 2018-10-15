from api import ApiHandler
from domain.image_randomizer import get_random_image_set

class GetImageSetHandler(ApiHandler):
    def _process(self):
        return {'images': get_random_image_set(2)} 