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

    OUTPUT_PACKET_LENGHT = 512

    KEY_COLS = 5
    KEY_ROWS = 3
    KEY_COUNT = KEY_COLS * KEY_ROWS

    KEY_PIXEL_WIDTH = 100
    KEY_PIXEL_HEIGHT = 100
    KEY_IMAGE_FORMAT = "JPEG"
    KEY_FLIP = (False, False)
    KEY_ROTATION = 180

    SCREEN_PIXEL_WIDTH = 800
    SCREEN_PIXEL_HEIGHT = 480
    SCREEN_IMAGE_FORMAT = "JPEG"
    SCREEN_FLIP = (False, False)
    SCREEN_ROTATION = 180

    DECK_TYPE = "Mirabox Stream Dock 293"
    DECK_VISUAL = True
    DECK_TOUCH = False

    KEY_NUM_TO_DEVICE_KEY_ID = [
                                    0x0d, 0x0a, 0x07, 0x04, 0x01
                                ,   0x0e, 0x0b, 0x08, 0x05, 0x02
                                ,   0x0f, 0x0c, 0x09, 0x06, 0x03
                            ]
    DEVICE_KEY_ID_TO_KEY_NUM = {value: index for index, value in enumerate(KEY_NUM_TO_DEVICE_KEY_ID)}


    def __init__(self, device):
        super().__init__(device)

        # see note in _read_control_states() method.
        self._key_triggered_last_read = False

    def _read_control_states(self):
        states = [False] * self.KEY_COUNT

        # _key_triggered_last_read exists since 293S only triggers an HID event when a button is released.
        # there are no key down and key up events, so we have to simulate the key being pressed and released.
        # if a firmware upgrade that supports key down/up events is released, this variable can be removed from the code.

        if not self._key_triggered_last_read:
            device_input_data = self.device.read(self.INPUT_PACKET_LENGHT)
            if device_input_data is None:
                return None

            if(device_input_data.startswith(Mirabox.ACK_OK)):
                triggered_raw_key = int.from_bytes(device_input_data[9:10], 'big', signed=False)
                triggered_key = self.DEVICE_KEY_ID_TO_KEY_NUM[triggered_raw_key]
            else:
                # we don't know how to handle the response
                return None

            states[triggered_key] = True

        self._key_triggered_last_read = not self._key_triggered_last_read

        return {
            ControlType.KEY: states
        }

    def set_key_image(self, key, image):
        if min(max(key, 0), self.KEY_COUNT) != key:
            raise IndexError("Invalid key index {}.".format(key))

        key = self.KEY_NUM_TO_DEVICE_KEY_ID[key]
        self._set_raw_key_image(key, image)

    def set_secondary_image(self, key, image):
       pass
