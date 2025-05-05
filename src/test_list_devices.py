#!/usr/bin/env python3

#         Python Stream Doeck Library
#      Released under the GPLv2 license
#
#  Authors:
#    * Lisias T (https://github.com/lisias)
#    * https://github.com/core447
#    * https://github.com/abcminiuser
#    * dean [at] fourwalledcubicle [dot] com
#

# Test script listing all devices in the USB pool

from StreamDeck.DeviceManager import DeviceManager

if __name__ == '__main__':
    dm = DeviceManager()

    devices = dm.transport.enumerate(None, None)
    print("Found {} USB Device(s).".format(len(devices)))
    for d in devices:
        print("\t{}:".format(repr(d)))

    print()
    streamdecks = dm.enumerate()
    print("Found {} Stream Deck(s).".format(len(streamdecks)))
    for sd in streamdecks:
        print("\t{}:".format(repr(sd.device)))
        print("\t\t{} with {} ".format(sd.deck_type(), "Visual Buttons" if sd.is_visual() else "Keys Only"))
        print("\t\tKey Count: {}".format(sd.key_count()))
        print("\t\tTouch Count: {}".format(sd.touch_key_count()))
        print("\t\tDial Count: {}".format(sd.dial_count()))
        print("\t\tSecondary Image Count: {}".format(sd.secondary_image_count()))
