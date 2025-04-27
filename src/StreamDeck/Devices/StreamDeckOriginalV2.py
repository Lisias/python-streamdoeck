#         Python Stream Doeck Library
#      Released under the GPLv2 license
#
#  Authors:
#    * Lisias T (https://github.com/lisias)
#    * https://github.com/core447
#    * https://github.com/abcminiuser
#    * dean [at] fourwalledcubicle [dot] com

from ..ImageHelpers import ImageTools
from .StreamDeck import StreamDeck, ControlType


class StreamDeckOriginalV2(StreamDeck):
    """
    Represents a physically attached StreamDeck Original (V2) device.
    """

    KEY_COUNT = 15
    KEY_COLS = 5
    KEY_ROWS = 3

    KEY_PIXEL_WIDTH = 72
    KEY_PIXEL_HEIGHT = 72
    KEY_IMAGE_FORMAT = "JPEG"
    KEY_FLIP = (True, True)
    KEY_ROTATION = 0

    DECK_TYPE = "Stream Deck Original"
    DECK_VISUAL = True

    IMAGE_REPORT_LENGTH = 1024
    IMAGE_REPORT_HEADER_LENGTH = 8
    IMAGE_REPORT_PAYLOAD_LENGTH = IMAGE_REPORT_LENGTH - IMAGE_REPORT_HEADER_LENGTH

    BLANK_KEY_IMAGE = ImageTools.load_asset("black-72x72.jpg")


    def _read_control_states(self):
        states = self.device.read(4 + self.KEY_COUNT)
        if states is None:
            return None

        states = states[4:]
        return {
            ControlType.KEY: [bool(s) for s in states]
        }

    def _reset_key_stream(self):
        payload = bytearray(self.IMAGE_REPORT_LENGTH)
        payload[0] = 0x02
        self.device.write(payload)

    def reset(self):
        payload = bytearray(32)
        payload[0:2] = [0x03, 0x02]
        self.device.write_feature(payload)

    def set_brightness(self, percent):
        if isinstance(percent, float):
            percent = int(100.0 * percent)

        percent = min(max(percent, 0), 100)

        payload = bytearray(32)
        payload[0:2] = [0x03, 0x08, percent]
        self.device.write_feature(payload)

    def get_serial_number(self):
        serial = self.device.read_feature(0x06, 32)
        return self._extract_string(serial[2:])

    def get_firmware_version(self):
        version = self.device.read_feature(0x05, 32)
        return self._extract_string(version[6:])

    def set_key_image(self, key, image):
        if min(max(key, 0), self.KEY_COUNT) != key:
            raise IndexError("Invalid key index {}.".format(key))

        image = bytes(image or self.BLANK_KEY_IMAGE)

        page_number = 0
        bytes_remaining = len(image)
        while bytes_remaining > 0:
            this_length = min(bytes_remaining, self.IMAGE_REPORT_PAYLOAD_LENGTH)
            bytes_sent = page_number * self.IMAGE_REPORT_PAYLOAD_LENGTH

            header = [
                0x02,
                0x07,
                key,
                1 if this_length == bytes_remaining else 0,
                this_length & 0xFF,
                this_length >> 8,
                page_number & 0xFF,
                page_number >> 8
            ]

            payload = bytes(header) + image[bytes_sent:bytes_sent + this_length]
            padding = bytearray(self.IMAGE_REPORT_LENGTH - len(payload))
            self.device.write(payload + padding)

            bytes_remaining = bytes_remaining - this_length
            page_number = page_number + 1

    def set_secondary_image(self, key, image):
        pass

    def set_touchscreen_image(self, image, x_pos=0, y_pos=0, width=0, height=0):
        pass

    def set_key_color(self, key, r, g, b):
        pass

    def set_screen_image(self, image):
        pass
