#         Python Stream Doeck Library
#      Released under the GPLv2 licence
#
#  Authors:
#    * Lisias T (https://github.com/lisias)
#    * Renato Schmidt (github.com/rescbr)
#
#  Mirabox Stream Dock Generic non-official support

from .StreamDeck import StreamDeck, ControlType
import sys


class Mirabox(StreamDeck):
    """
    Abstract class for Mirabox Stream Dock devices.
    """

    INPUT_PACKET_LENGHT = 512
    MAX_IMAGE_SIZE = 10240

    CMD_PREFIX = bytes([0x43, 0x52, 0x54, 0x00, 0x00])              # CRT\0\0
    CRT_CONNECT = bytes([0x43, 0x4f, 0x4e, 0x4e, 0x45, 0x43, 0x54]) # CRT\0\0CONNECT
    CRT_LIG = bytes([0x4c, 0x49, 0x47, 0x00, 0x00])                 # CRT\0\0LIG 0x00 0x00 <PERCENT>
    CRT_CLE = bytes([0x43, 0x4c, 0x45, 0x00, 0x00, 0x00])           # CRT\0\0CLE 0x00 0x00 0x00 <KEY ID | 0xff for all>
    CRT_DIS = bytes([0x44, 0x49, 0x53])                             # CRT\0\0DIS
    CRT_BAT = bytes([0x42, 0x41, 0x54, 0x00, 0x00])                 # CRT\0\0BAT 0x00 0x00 <image size uint16_be> <key id>
    CRT_STP = bytes([0x53, 0x54, 0x50])                             # CRT\0\0STP
    CRT_LOG = bytes([0x4c, 0x4f, 0x47])                             # CRT\0\0LOG <image size uint32_be> <screen id>
    CRT_CLOSE = bytes([0x43, 0x4c, 0x45, 0x00, 0x44, 0x43])         # CRT\0\0CLE 0x00 0x00 0x44 0x43
    CRT_HANG = bytes([0x48, 0x41, 0x4e])                            # CRT\0\0HAN
    ACK_OK = bytes([0x41, 0x43, 0x4b, 0x00, 0x00, 0x4f, 0x4b, 0x00])    # ACK\0\0OK\0

    def __init__(self, device):
        super().__init__(device)

    def _make_payload_for_report_id(self, report_id, payload_data):
        payload = bytearray(self.OUTPUT_PACKET_LENGHT + 1)
        payload[0] = report_id
        payload[1:len(payload_data)] = payload_data
        return payload

    def _reset_key_stream(self):
        self.reset()

    def _check_ack_ok(self, msg, *args):
        device_input_data = self.device.read(self.INPUT_PACKET_LENGHT)
        if(not (device_input_data and device_input_data.startswith(Mirabox.ACK_OK))):
            msg = msg.format(*args)
            print(msg, repr(device_input_data), file=sys.stderr)
            raise IOError(msg)

    def reset(self):
        # disconnect
        payload = self._make_payload_for_report_id(0x00, Mirabox.CMD_PREFIX + Mirabox.CRT_DIS)
        self.device.write(payload)

        # connect/ping
        payload = self._make_payload_for_report_id(0x00, Mirabox.CMD_PREFIX + Mirabox.CRT_CONNECT)
        self.device.write(payload)

        # clear contents
        payload = self._make_payload_for_report_id(0x00, Mirabox.CMD_PREFIX + Mirabox.CRT_CLE + bytes([0xff]))
        self.device.write(payload)

    def close(self):
        payload = self._make_payload_for_report_id(0x00, Mirabox.CMD_PREFIX + Mirabox.CRT_CLOSE)
        self.device.write(payload)
        payload = self._make_payload_for_report_id(0x00, Mirabox.CMD_PREFIX + Mirabox.CRT_HANG)
        super().close()

    def set_brightness(self, percent):
        if isinstance(percent, float):
            percent = int(100.0 * percent)

        percent = min(max(percent, 0), 100)

        # set brightness
        payload = self._make_payload_for_report_id(0x00, Mirabox.CMD_PREFIX + Mirabox.CRT_LIG + bytes([percent]))
        self.device.write(payload)

    def get_serial_number(self):
        return self.device.serial_number()

    def get_firmware_version(self):
        version = self.device.read_input(0x00, self.OUTPUT_PACKET_LENGHT + 1)
        return self._extract_string(version[1:])

    def _set_raw_key_image(self, key, image):
        image_size = len(image)
        if image_size > self.MAX_IMAGE_SIZE:
            raise IOError("Image bigger than max allowed size ({})".format(self.MAX_IMAGE_SIZE))

        image_payload_page_length = self.OUTPUT_PACKET_LENGHT
        image_size_uint16_be = int.to_bytes(len(image), 2, 'big', signed=False)

        # start batch
        command = Mirabox.CMD_PREFIX + Mirabox.CRT_BAT + image_size_uint16_be + bytes([key])
        payload = self._make_payload_for_report_id(0x00, command)
        self.device.write(payload)

        page_number = 0
        bytes_remaining = image_size
        while bytes_remaining > 0:
            this_length = min(bytes_remaining, image_payload_page_length)
            bytes_sent = page_number * image_payload_page_length

            #send data
            payload = self._make_payload_for_report_id(0x00, image[bytes_sent:bytes_sent + this_length])
            self.device.write(payload)

            bytes_remaining = bytes_remaining - this_length
            page_number = page_number + 1

        # stop batch
        payload = self._make_payload_for_report_id(0x00, Mirabox.CMD_PREFIX + Mirabox.CRT_STP)
        self.device.write(payload)

    def set_touchscreen_image(self, image, x_pos=0, y_pos=0, width=0, height=0):
        pass

    def set_key_color(self, key, r, g, b):
        pass

    def _set_screen_image(self, image:bytes):
        image_payload_page_length = self.OUTPUT_PACKET_LENGHT
        image_size_uint32_be = int.to_bytes(len(image), 4, 'big', signed=False)

        # start logo
        command = Mirabox.CMD_PREFIX + Mirabox.CRT_LOG + image_size_uint32_be + bytes([1])
        payload = self._make_payload_for_report_id(0x00, command)
        self.device.write(payload)

        page_number = 0
        bytes_remaining = len(image)
        while bytes_remaining > 0:
            this_length = min(bytes_remaining, image_payload_page_length)
            bytes_sent = page_number * image_payload_page_length

            #send data
            payload = self._make_payload_for_report_id(0x00, image[bytes_sent:bytes_sent + this_length])
            self.device.write(payload)

            bytes_remaining = bytes_remaining - this_length
            page_number = page_number + 1

        # stop batch
        payload = self._make_payload_for_report_id(0x00, Mirabox.CMD_PREFIX + Mirabox.CRT_STP)
        self.device.write(payload)

        self._check_ack_ok("set_screen_image failed.")
