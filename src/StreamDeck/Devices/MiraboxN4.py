#         Python Stream Doeck Library
#      Released under the GPLv2 licence
#
#  Authors:
#    * Lisias T (https://github.com/lisias)
#
#  Mirabox Stream Dock N4 non-official support

from ..ImageHelpers import ImageTools
from .StreamDeck import StreamDeck, ControlType, DialEventType
from .Mirabox import Mirabox

class MiraboxN4(Mirabox):
    """
    Represents a physically attached Mirabox Stream Dock 293 device.
    """

    OUTPUT_PACKET_LENGHT = 1024

    KEY_COLS = 5
    KEY_ROWS = 2
    KEY_COUNT = KEY_COLS * KEY_ROWS

    KEY_PIXEL_WIDTH = 126
    KEY_PIXEL_HEIGHT = 126
    KEY_IMAGE_FORMAT = "JPEG"
    KEY_FLIP = (False, False)
    KEY_ROTATION = 180

    TOUCH_KEY_COUNT = 6

    SECONDARY_IMAGE_COLS = 1
    SECONDARY_IMAGE_ROWS = 4
    SECONDARY_IMAGE_COUNT = SECONDARY_IMAGE_ROWS * SECONDARY_IMAGE_COLS

    SECONDARY_IMAGE_PIXEL_WIDTH = 176
    SECONDARY_IMAGE_PIXEL_HEIGHT = 112
    SECONDARY_IMAGE_IMAGE_FORMAT = "JPEG"
    SECONDARY_IMAGE_FLIP = (False, False)
    SECONDARY_IMAGE_ROTATION = 180

    SCREEN_PIXEL_WIDTH = 800
    SCREEN_PIXEL_HEIGHT = 480
    SCREEN_IMAGE_FORMAT = "JPEG"
    SCREEN_FLIP = (False, False)
    SCREEN_ROTATION = 180

    DIAL_COUNT = 4

    DECK_TYPE = "Mirabox Stream Dock N4"
    DECK_VISUAL = True
    DECK_TOUCH = False

#    BLANK_KEY_IMAGE = ImageTools.load_asset("black-126x126.jpg")
#    BLANK_SECONDARY_IMAGE = ImageTools.load_asset("black-176x112.jpg")

    KEY_NUM_TO_DEVICE_KEY_ID = [
                                    0x01, 0x02, 0x03, 0x04, 0x05
                                ,   0x06, 0x07, 0x08, 0x09, 0x0a
                            ]
    KEY_DEVICE_ID_TO_KEY_NUM = {value: index for index, value in enumerate(KEY_NUM_TO_DEVICE_KEY_ID)}

    TOUCH_NUM_TO_DEVICE_TOUCH_ID = [
                                    0x38, 0x39                      # swipe left, swipe right
                                ,   0x40, 0x41, 0x42, 0x43          # Touch Keys
                            ]
    TOUCH_DEVICE_ID_TO_TOUCH_NUM = {value: index for index, value in enumerate(TOUCH_NUM_TO_DEVICE_TOUCH_ID)}

    DIAL_NUM_PUSH_TO_DEVICE_KEY_ID = [0x37, 0x35, 0x33, 0x36]
    KEY_DEVICE_ID_TO_DIAL_PUSH_NUM = {value: index for index, value in enumerate(DIAL_NUM_PUSH_TO_DEVICE_KEY_ID)}

    DIAL_TURN_LEFT_NUM_TO_DEVICE_KEY_ID = [0xa0, 0x50, 0x90, 0x70]
    KEY_DEVICE_ID_TO_DIAL_TURN_LEFT_NUM = {value: index for index, value in enumerate(DIAL_TURN_LEFT_NUM_TO_DEVICE_KEY_ID)}

    DIAL_TURN_RIGHT_NUM_TO_DEVICE_KEY_ID = [0xa1, 0x51, 0x91, 0x71]
    KEY_DEVICE_ID_TO_DIAL_TURN_RIGHT_NUM = {value: index for index, value in enumerate(DIAL_TURN_RIGHT_NUM_TO_DEVICE_KEY_ID)}

    def __init__(self, device):
        super().__init__(device)

    def _read_control_states(self):
        device_input_data = self.device.read(self.INPUT_PACKET_LENGHT)
        if device_input_data is None:
            return None

        if(device_input_data.startswith(Mirabox.ACK_OK)):
            triggered_raw_key = device_input_data[9]
            triggered_state = device_input_data[10]

            if triggered_raw_key in self.KEY_NUM_TO_DEVICE_KEY_ID:
                states = [False] * (self.KEY_COUNT + self.TOUCH_KEY_COUNT)
                triggered_key = self.KEY_DEVICE_ID_TO_KEY_NUM[triggered_raw_key]
                states[triggered_key] = 1 == triggered_state
                return {
                    ControlType.KEY: states,
                }

            elif triggered_raw_key in self.TOUCH_NUM_TO_DEVICE_TOUCH_ID:
                states = [False] * (self.KEY_COUNT + self.TOUCH_KEY_COUNT)
                triggered_key = len(self.KEY_DEVICE_ID_TO_KEY_NUM) + self.TOUCH_DEVICE_ID_TO_TOUCH_NUM[triggered_raw_key]
                states[triggered_key] = True
                return {
                    ControlType.TOUCH_KEY: states,
                }

            elif triggered_raw_key in self.DIAL_NUM_PUSH_TO_DEVICE_KEY_ID:
                states = [False] * self.DIAL_COUNT
                triggered_key = self.KEY_DEVICE_ID_TO_DIAL_PUSH_NUM[triggered_raw_key]
                states[triggered_key] = True
                return {
                    ControlType.DIAL: {
                        DialEventType.PUSH : states
                    }
                }

            elif triggered_raw_key in self.DIAL_TURN_LEFT_NUM_TO_DEVICE_KEY_ID:
                states = [0] * self.DIAL_COUNT
                triggered_key = self.KEY_DEVICE_ID_TO_DIAL_TURN_LEFT_NUM[triggered_raw_key]
                states[triggered_key] = -1
                return {
                    ControlType.DIAL: {
                        DialEventType.TURN : states
                    }
                }

            elif triggered_raw_key in self.DIAL_TURN_RIGHT_NUM_TO_DEVICE_KEY_ID:
                states = [0] * self.DIAL_COUNT
                triggered_key = self.KEY_DEVICE_ID_TO_DIAL_TURN_RIGHT_NUM[triggered_raw_key]
                states[triggered_key] = +1
                return {
                    ControlType.DIAL: {
                        DialEventType.TURN : states
                    }
                }

        # we don't know how to handle the response
        return None

    def set_key_image(self, key, image):
        if min(max(key, 0), self.KEY_COUNT) != key:
            raise IndexError("Invalid key index {}.".format(key))

        key = self.KEY_NUM_TO_DEVICE_KEY_ID[key]
        self._set_raw_key_image(key, image)

    def set_secondary_image(self, key, image):
        pass

    def set_screen_image(self, image:bytes):
        pass