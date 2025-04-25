#         Python Stream Doeck Library
#      Released under the GPLv2 licence
#
#  Authors:
#    * Lisias T (https://github.com/lisias)
#
#  Mirabox Stream Dock 293 non-official support

from .StreamDeck import StreamDeck, ControlType
from .Mirabox import Mirabox

class Mirabox293(Mirabox):
    """
    Represents a physically attached Mirabox Stream Dock 293 device.
    """

    KEY_COLS = 5
    KEY_ROWS = 3
    KEY_COUNT = KEY_COLS * KEY_ROWS

    KEY_PIXEL_WIDTH = 85 # TODO: check if this is the correct value
    KEY_PIXEL_HEIGHT = 85 # TODO: check if this is the correct value
    KEY_IMAGE_FORMAT = "JPEG"
    KEY_FLIP = (False, False)
    KEY_ROTATION = 90

    SCREEN_PIXEL_WIDTH = 800
    SCREEN_PIXEL_HEIGHT = 480
    SCREEN_IMAGE_FORMAT = "JPEG"
    SCREEN_FLIP = (True, False)
    SCREEN_ROTATION = 0

    DECK_TYPE = "Mirabox Stream Dock 293"
    DECK_VISUAL = True
    DECK_TOUCH = False

    KEY_NUM_TO_DEVICE_KEY_ID = [
                                    0x0d, 0x0a, 0x07, 0x04, 0x01
                                ,   0x0e, 0x0b, 0x08, 0x05, 0x02
                                ,   0x0f, 0x0c, 0x09, 0x06, 0x03
                            ]
    KEY_DEVICE_KEY_ID_TO_NUM = {value: index for index, value in enumerate(KEY_NUM_TO_DEVICE_KEY_ID)}

    def _convert_key_num_to_device_key_id(self, key):
        return self.KEY_NUM_TO_DEVICE_KEY_ID[key]

    def _convert_device_key_id_to_key_num(self, key):
        return self.KEY_DEVICE_KEY_ID_TO_NUM[key]

    def set_secondary_image(self, key, image):
       pass
