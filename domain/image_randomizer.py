import random
import os
import logging

def get_random_image_set(number_of_images, images = []):
    for i in range(0, number_of_images):
        image = get_random_image()
        if image in images:
            new_images = get_random_image_set(number_of_images-i, images)
        else:
            new_images = [image]
        images.extend(new_images)
        logging.info(new_images)
    return images

def get_random_image():
    images = _get_images()
    image = images[random.randint(0,len(images)-1)]
    return _format_static_image_path(image)

def _get_images():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    images_dir = os.path.join(current_dir, os.pardir, 'static', 'images')
    return os.listdir(images_dir)

def _format_static_image_path(path):
    return os.path.join('static', 'images', path)
    