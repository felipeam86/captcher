"""
"""

from captcher.image import background
from captcher.image import captcha
from captcher.image import curve
from captcher.image import noise
from captcher.image import offset
from captcher.image import rotate
from captcher.image import smooth
from captcher.image import text
from captcher.image import warp


if __name__ == '__main__':
    import random
    import string
    captcha_image = captcha(drawings=[
        background(),
        text(fonts=[
            'fonts/CourierNew-Bold.ttf',
            'fonts/LiberationMono-Bold.ttf'],
            drawings=[
                warp(),
                rotate(),
                offset()
            ]),
        curve(),
        noise(),
        smooth()
    ])
    image = captcha_image(random.sample(string.ascii_uppercase + string.digits, 4))
    image.save('sample.jpg', 'JPEG', quality=75)
