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

# Example script showing how to set up the LOGO image

import sys
import threading

from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import ImageTools, NativeImageHelper
from StreamDeck.Transport.Transport import TransportError


# Closes the StreamDeck device on key state change.
def key_change_callback(deck, key, state):
    if not state: return

    # Use a scoped-with on the deck to ensure we're the only thread using it
    # right now.
    with deck:
        # Reset deck, clearing all button images.
        deck.reset()

        # Close deck handle, terminating internal worker threads.
        deck.close()


if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    print("This program permanently changes the device's boot screen (when possible)")
    print("and so it was found safer to prevent it from being ran by accident -")
    print("unless you have a copy of the original boot screen, the change **IS NOT**")
    print("reversible!")
    print("")
    print("Remove or comment the `sys.exit` instruction you will find below these")
    print("`print` instructions to run it. You can upload any image you want,")
    print("by the way, as long the file format it's support by `pillow`.")
    sys.exit(0)

    for index, deck in enumerate(streamdecks):
        # This example only works with devices that have screens.
        if not deck.is_visual():
            continue

        deck.open()
        deck.reset()

        print("Opened '{}' device (serial number: '{}')".format(deck.deck_type(), deck.get_serial_number()))

        # Set initial screen brightness to 30%.
        deck.set_brightness(30)

        # Load and resize a source image so that it will fill the given
        # StreamDeck.
        image = ImageTools.load_asset_image("S65-63220-large.jpg")
        print("Loaded image with {}x{} pixels.".format(image.width, image.height))
        image = ImageTools.adjust_image(image, deck.screen_image_format())
        print("Adjusted image to {}x{} pixels.".format(image.width, image.height))

#        image.save(os.path.expanduser("~/temp/image.png"))
        with deck:
            deck.set_screen_image(image.tobytes())

        print("Ready.")

        # Register callback function for when a key state changes.
        deck.set_key_callback(key_change_callback)

        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        for t in threading.enumerate():
            try:
                t.join()
            except (TransportError, RuntimeError):
                pass
