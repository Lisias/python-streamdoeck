#         Python Stream Doeck Library
#      Released under the GPLv2 license
#
#  Authors:
#    * Lisias T (https://github.com/lisias)
#    * https://github.com/core447
#    * https://github.com/abcminiuser
#    * dean [at] fourwalledcubicle [dot] com
#

import io
from . import ImageTools


def _to_native_format(image, image_format):
    image = ImageTools.adjust_image(image, image_format)

    # We want a compressed image in a given codec, convert.
    with io.BytesIO() as compressed_image:
        image.save(compressed_image, image_format['format'], quality=100)
        return compressed_image.getvalue()


def create_image(image_format:dict, background='black'):
    """
    Creates a new PIL Image with the given image dimensions.

    .. seealso:: See :func:`~NativeImageHelper.to_native_format` method for converting a
                 PIL image instance to the native key image format

    :param dict image_format: the image format
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtype: PIL.Image
    :return: Created PIL image
    """
    return ImageTools.create_image(image_format, background)


def create_key_image(deck, background='black'):
    """
    Creates a new PIL Image with the correct image dimensions for the given
    StreamDeck device's keys.

    .. seealso:: See :func:`~NativeImageHelper.to_native_key_format` method for converting a
                 PIL image instance to the native key image format of a given
                 StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible image for.
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtype: PIL.Image
    :return: Created PIL image
    """
    return create_image(deck.key_image_format(), background)


def create_secondary_image(deck, background='black'):
    """
    Creates a new PIL Image with the correct image dimensions for the given
    StreamDeck device's touch keys.

    .. seealso:: See :func:`~NativeImageHelper.to_native_key_format` method for converting a
                 PIL image instance to the native key image format of a given
                 StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible image for.
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtype: PIL.Image
    :return: Created PIL image
    """
    return create_image(deck.secondary_image_format(), background)


def create_touchscreen_image(deck, background='black'):
    """
    Creates a new PIL Image with the correct image dimensions for the given
    StreamDeck device's touchscreen.

    .. seealso:: See :func:`~NativeImageHelper.to_native_touchscreen_format` method for converting a
                 PIL image instance to the native touchscreen image format of a given
                 StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible image for.
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtype: PIL.Image
    :return: Created PIL image
    """
    return create_image(deck.touchscreen_image_format(), background)


def create_screen_image(deck, background='black'):
    """
    Creates a new PIL Image with the correct image dimensions for the given
    StreamDeck device's creen.

    .. seealso:: See :func:`~NativeImageHelper.to_native_screen_format` method for converting a
                 PIL image instance to the native screen image format of a given
                 StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible image for.
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtype: PIL.Image
    :return: Created PIL image
    """
    return create_image(deck.screen_image_format(), background)


def create_scaled_image(image_format, image, margins=[0, 0, 0, 0], background='black'):
    """
    """
    return ImageTools.scale_image(image, image_format, margins, background)


def create_scaled_key_image(deck, image, margins=[0, 0, 0, 0], background='black'):
    """
    Creates a new key image that contains a scaled version of a given image,
    resized to best fit the given StreamDeck device's keys with the given
    margins around each side.

    The scaled image is centered within the new key image, offset by the given
    margins. The aspect ratio of the image is preserved.

    .. seealso:: See :func:`~NativeImageHelper.to_native_key_format` method for converting a
                 PIL image instance to the native key image format of a given
                 StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible image for.
    :param Image image: PIL Image object to scale
    :param list(int): Array of margin pixels in (top, right, bottom, left) order.
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtrype: PIL.Image
    :return: Loaded PIL image scaled and centered
    """
    return ImageTools.scale_image(image, deck.key_image_format(), margins, background)


def create_scaled_secondary_image(deck, image, margins=[0, 0, 0, 0], background='black'):
    """
    Creates a new key image that contains a scaled version of a given image,
    resized to best fit the given StreamDeck device's keys with the given
    margins around each side.

    The scaled image is centered within the new key image, offset by the given
    margins. The aspect ratio of the image is preserved.

    .. seealso:: See :func:`~NativeImageHelper.to_native_key_format` method for converting a
                 PIL image instance to the native key image format of a given
                 StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible image for.
    :param Image image: PIL Image object to scale
    :param list(int): Array of margin pixels in (top, right, bottom, left) order.
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtrype: PIL.Image
    :return: Loaded PIL image scaled and centered
    """
    return ImageTools.scale_image(image, deck.touch.key_image_format(), margins, background)


def create_scaled_touchscreen_image(deck, image, margins=[0, 0, 0, 0], background='black'):
    """
    Creates a new touchscreen image that contains a scaled version of a given image,
    resized to best fit the given StreamDeck device's touchscreen with the given
    margins around each side.

    The scaled image is centered within the new touchscreen image, offset by the given
    margins. The aspect ratio of the image is preserved.

    .. seealso:: See :func:`~NativeImageHelper.to_native_touchscreen_format` method for converting a
                 PIL image instance to the native key image format of a given
                 StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible image for.
    :param Image image: PIL Image object to scale
    :param list(int): Array of margin pixels in (top, right, bottom, left) order.
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtrype: PIL.Image
    :return: Loaded PIL image scaled and centered
    """
    return ImageTools.scale_image(image, deck.touchscreen_image_format(), margins, background)


def create_scaled_screen_image(deck, image, margins=[0, 0, 0, 0], background='black'):
    """
    Creates a new screen image that contains a scaled version of a given image,
    resized to best fit the given StreamDeck device's screen with the given
    margins around each side.

    The scaled image is centered within the new screen image, offset by the given
    margins. The aspect ratio of the image is preserved.

    .. seealso:: See :func:`~NativeImageHelper.to_native_screen_format` method for converting a
                 PIL image instance to the native key image format of a given
                 StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible image for.
    :param Image image: PIL Image object to scale
    :param list(int): Array of margin pixels in (top, right, bottom, left) order.
    :param str background: Background color to use, compatible with `PIL.Image.new()`.

    :rtrype: PIL.Image
    :return: Loaded PIL image scaled and centered
    """
    return ImageTools.scale_image(image, deck.screen_image_format(), margins, background)


def to_native_format(image_format:dict, image):
    """
    """
    return _to_native_format(image, image_format)


def to_native_key_format(deck, image):
    """
    Converts a given PIL image to the native key image format for a StreamDeck,
    suitable for passing to :func:`~StreamDeck.set_key_image`.

    .. seealso:: See :func:`~NativeImageHelper.create_image` method for creating a PIL
                 image instance for a given StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible native image for.
    :param PIL.Image image: PIL Image to convert to the native StreamDeck image format

    :rtype: enumerable()
    :return: Image converted to the given StreamDeck's native format
    """
    return _to_native_format(image, deck.key_image_format())


def to_native_secondary_image_format(deck, image):
    """
    Converts a given PIL image to the native touch key image format for a StreamDeck,
    suitable for passing to :func:`~StreamDeck.set_key_image`.

    .. seealso:: See :func:`~NativeImageHelper.create_image` method for creating a PIL
                 image instance for a given StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible native image for.
    :param PIL.Image image: PIL Image to convert to the native StreamDeck image format

    :rtype: enumerable()
    :return: Image converted to the given StreamDeck's native format
    """
    return _to_native_format(image, deck.secondary_image_format())


def to_native_touchscreen_format(deck, image):
    """
    Converts a given PIL image to the native touchscreen image format for a StreamDeck,
    suitable for passing to :func:`~StreamDeck.set_touchscreen_image`.

    .. seealso:: See :func:`~NativeImageHelper.create_touchscreen_image` method for creating a PIL
                 image instance for a given StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible native image for.
    :param PIL.Image image: PIL Image to convert to the native StreamDeck image format

    :rtype: enumerable()
    :return: Image converted to the given StreamDeck's native touchscreen format
    """
    return _to_native_format(image, deck.touchscreen_image_format())


def to_native_screen_format(deck, image):
    """
    Converts a given PIL image to the native screen image format for a StreamDeck,
    suitable for passing to :func:`~StreamDeck.set_screen_image`.

    .. seealso:: See :func:`~NativeImageHelper.create_screen_image` method for creating a PIL
                 image instance for a given StreamDeck device.

    :param StreamDeck deck: StreamDeck device to generate a compatible native image for.
    :param PIL.Image image: PIL Image to convert to the native StreamDeck image format

    :rtype: enumerable()
    :return: Image converted to the given StreamDeck's native screen format
    """
    return _to_native_format(image, deck.screen_image_format())
