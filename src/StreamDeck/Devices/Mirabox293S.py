#         Python Stream Doeck Library
#      Released under the GPLv2 licence
#
#  Authors:
#    * Lisias T (https://github.com/lisias)
#    * Renato Schmidt (github.com/rescbr)
#
#  Mirabox Stream Dock 293S non-official support

from .StreamDeck import StreamDeck, ControlType
from .Mirabox293 import Mirabox293


class Mirabox293S(Mirabox293):
    """
    Represents a physically attached Mirabox Stream Dock 293S device.
    """

    SECONDARY_IMAGE_COLS = 1
    SECONDARY_IMAGE_ROWS = 3
    SECONDARY_IMAGE_COUNT = SECONDARY_IMAGE_ROWS * SECONDARY_IMAGE_COLS

    SECONDARY_IMAGE_PIXEL_WIDTH = 80
    SECONDARY_IMAGE_PIXEL_HEIGHT = 80
    SECONDARY_IMAGE_IMAGE_FORMAT = "JPEG"
    SECONDARY_IMAGE_FLIP = (False, False)
    SECONDARY_IMAGE_ROTATION = 90

    SCREEN_PIXEL_WIDTH = 854

    DECK_TYPE = "Mirabox Stream Dock 293S"
    DECK_VISUAL = True
    DECK_TOUCH = False # kind of... it could be used for the side display.

    # the side display uses key ids 0x10, 0x11, 0x12 with 80x80 images.
    SECONDARY_IMAGE_NUM_TO_DEVICE_KEY_ID = [0x10, 0x11, 0x12]

    def __init__(self, device):
        super().__init__(device)

    def _convert_key_num_to_device_key_id(self, key):
        return self.KEY_NUM_TO_DEVICE_KEY_ID[key]

    def _convert_device_key_id_to_key_num(self, key):
        return self.KEY_DEVICE_KEY_ID_TO_NUM[key]

    def _convert_secondary_image_num_to_device_key_id(self, key):
        return self.SECONDARY_IMAGE_NUM_TO_DEVICE_KEY_ID[key]

    def set_secondary_image(self, key, image):
        if min(max(key, 0), self.SECONDARY_IMAGE_COUNT) != key:
            raise IndexError("Invalid secondary image  index {}.".format(key))

        key = self._convert_secondary_image_num_to_device_key_id(key)
        self._set_raw_key_image(key, image)
