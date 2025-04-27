#         Python Stream Doeck Library
#      Released under the GPLv2 licence
#
#  Authors:
#    * Lisias T (https://github.com/lisias)
#    * Renato Schmidt (github.com/rescbr)
#
#  Mirabox Stream Dock 293S non-official support

from ..ImageHelpers import ImageTools
from .StreamDeck import StreamDeck, ControlType
from .Mirabox import Mirabox
from .Mirabox293 import Mirabox293


class Mirabox293S(Mirabox293):
    """
    Represents a physically attached Mirabox Stream Dock 293S device.
    """

    OUTPUT_PACKET_LENGHT = 512

    KEY_PIXEL_WIDTH = 85
    KEY_PIXEL_HEIGHT = 85
    KEY_IMAGE_FORMAT = "JPEG"
    KEY_FLIP = (False, False)
    KEY_ROTATION = 90

    SECONDARY_IMAGE_COLS = 1
    SECONDARY_IMAGE_ROWS = 3
    SECONDARY_IMAGE_COUNT = SECONDARY_IMAGE_ROWS * SECONDARY_IMAGE_COLS

    SECONDARY_IMAGE_PIXEL_WIDTH = 80
    SECONDARY_IMAGE_PIXEL_HEIGHT = 80
    SECONDARY_IMAGE_IMAGE_FORMAT = "JPEG"
    SECONDARY_IMAGE_FLIP = (False, False)
    SECONDARY_IMAGE_ROTATION = 90

    SCREEN_PIXEL_WIDTH = 854
    SCREEN_FLIP = (False, False)
    SCREEN_ROTATION = 90

    DECK_TYPE = "Mirabox Stream Dock 293S"
    DECK_VISUAL = True
    DECK_TOUCH = False  # kind of... it could be used for the side display.

    BLANK_KEY_IMAGE = ImageTools.load_asset("black-85x85.jpg")
    BLANK_SECONDARY_IMAGE = ImageTools.load_asset("black-80x80.jpg")

    # the side display uses key ids 0x10, 0x11, 0x12 with 80x80 images.
    SECONDARY_IMAGE_NUM_TO_DEVICE_KEY_ID = [0x10, 0x11, 0x12]

    def __init__(self, device):
        super().__init__(device)

    def set_key_image(self, key, image):
        if min(max(key, 0), self.KEY_COUNT) != key:
            raise IndexError("Invalid key index {}.".format(key))

        image = bytes(image or self.BLANK_KEY_IMAGE)
        key = self.KEY_NUM_TO_DEVICE_KEY_ID[key]
        self._set_raw_key_image(key, image)

    def set_secondary_image(self, key, image):
        if min(max(key, 0), self.SECONDARY_IMAGE_COUNT) != key:
            raise IndexError("Invalid secondary image  index {}.".format(key))

        image = bytes(image or self.BLANK_SECONDARY_IMAGE)
        key = self.SECONDARY_IMAGE_NUM_TO_DEVICE_KEY_ID[key]
        self._set_raw_key_image(key, image)

    def set_screen_image(self, image:bytes):
        image = bytearray(image)
        for i in range(0, len(image), 3):
            (image[i], image[i + 2]) = (image[i + 2], image[i])
        self._set_screen_image(image)