# Python Stream Doeck Library :: CHANGE LOG

* 2025-0323: Version 0.1.4 (Core744)
	- No change log provided
* 2025-0329: Version 0.1.3 (Core744)
	- `self.reconnect_after_suspend`
* 2025-0323: Version 0.1.2 (Core744)
	- Implement Resume From Suspend
	- Add Support for Mirabox Stream Dock 293S
* 2025-0323: Version 0.1 (Core744)
	- No change log provided
* 2024-1028: Version 0.9.6 (abcminiuser)
	- Fixed StreamDeck+ returning 10 key states instead of the expected 8.
	- Fixed StreamDeck+ dial push event not being detected correctly.
	- Fixed old key states and dial states returned if requested from inside a key or dial callback function.
	- Added support for FreeBSD platforms.
	- Added support for the StreamDeck Neo.
* 2023-1223: Version 0.9.5 (abcminiuser)
	- Added support for the StreamDeck Plus.
* 2023-0823: Version 0.9.4 (abcminiuser)
	- Updated Windows HIDAPI backend to attempt to load from the local working directory.
	- Added detection for MacOS Homebrew installations of the libhidapi back-end library.
* 2022-1016: Version 0.9.3 (abcminiuser)
	- Added support for a new sub-variant of the StreamDeck XL.
* 2022-1013: Version 0.9.2 (abcminiuser)
	- Added support for a new sub-variant of the StreamDeck Mini.
* 2022-0417: Version 0.9.1 (abcminiuser)
	- Transport errors now trigger a closing of the underlying StreamDeck device, so further API calls will throw correctly (and ``is_open()`` will return ``False``).
	- Updated animated example script to use separate cycle generators for each key, so the animations play at the correct rate regardless of key count.
	- Added support for the StreamDeck pedal.
	- Added new `is_visual()` function.
* 2022-0103: Version 0.9.0 (abcminiuser)
	- Added new `set_poll_frequency()` function.
	- Added new `is_open()` function.
	- Fixed a possible internal thread join error when a deck object was closed.
* 2021-0723: Version 0.8.5 (abcminiuser)
	- Add support for the new StreamDeck MK2.
2021-0404: Version 0.8.4 (abcminiuser)
	- Updated animated example script to attempt to maintain a constant FPS, regardless of rendering time.
	- Fixed a race condition in the LibUSB HIDAPI transport backend that could cause crashes when a device was closed.
* 2020-1121: Version 0.8.3 (abcminiuser)
	- Altered LibUSB transport workaround to only apply on Mac.
	- Fixed internal _extract_string() method to discard all data after the first NUL byte, fixing corrupt serial number strings being returned in some cases.
	- Set minimum Python version to 3.8, as some of the library uses newer syntax/core library features.
* 2020-0804: Version 0.8.2 (abcminiuser)
	- Added new ``PILHelper.create_scaled_image()`` function to easily generate scaled/padded key images for a given deck.
	- Updated LibUSB transport backend so that device paths are returned as UTF-8 strings, not raw bytes.
	- Updated version/serial number string extraction from StreamDecks so that invalid characters are substituted, rather than raising a ``UnicodeDecodeError`` error.
	- Added LibUSB transport workaround for a bug on Mac platforms when using older versions of the library.
* 2020-0516: Version 0.8.1 (abcminiuser)
	- Fixed memory leak in LibUSB HIDAPI transport backend.
* 2020-0515: Version 0.8.0 (abcminiuser)
	- Fix random crashes in LibUSB HIDAPI transport backend on Windows, as the API is not thread safe.
	- Added support for atomic updates of StreamDeck instances via the Python ``with`` scope syntax.
* 2020-0417: Version 0.7.3 (abcminiuser)
	- Fix crash in new LibUSB HIDAPI transport backend on systems with multiple connected StreamDeck devices.
	- Fix crash in new LibUSB HIDAPI transport backend when ``connected()`` was called on a StreamDeck instance.
* 2020-0411: Version 0.7.2 (abcminiuser)
	- Documentation restructuring to move installation out of the readme and into the library documentation.
* 2020-0411: Version 0.7.1 (abcminiuser)
	- Cleaned up new LibUSB HIDAPI transport backend, so that it only searches for OS-specific library files.
	- Fixed minor typo in the libUSB HIDAPI transport backend probe failure message.
* 2020-0409: Version 0.7.0 (abcminiuser)
	- Removed old HID and HIDAPI backends, added new ``ctypes`` based LibUSB-HIDAPI backend replacement.
* 2019-1121: Version 0.6.3 (abcminiuser)
	- Added support for the new V2 hardware revision of the StreamDeck Original.
* 2019-1116: Version 0.6.2 (abcminiuser)
	- Fixed broken StreamDeck XL communications on Linux.
	- Added blacklist for the ``libhidapi-hidraw`` system library which breaks StreamDeck Original communications.
* 2019-1022: Version 0.6.1 (abcminiuser)
	- Fixed broken HIDAPI backend probing.
	- Fixed double-open of HID backend devices causing connection issues on some platforms.
* 2019-1020: Version 0.6.0 (abcminiuser)
	- Added support for the ``HID`` Python package. This new HID backend is strongly recommended over the old HIDAPI backend.
	- Added auto-probing of installed backends, if no specific transport is supplied when constructing a DeviceManager instance.
* 2019-1009: Version 0.5.1 (abcminiuser)
	- Fixed StreamDeck XL reporting swapped rows/columns count.
	- Fixed StreamDeck XL failing to report correct serial number and firmware version.
* 2019-0918: Version 0.5.0 (abcminiuser)
	- Fixed StreamDeck devices occasionally showing partial old frames on initial connection.
	- Removed support for RAW pixel images, StreamDeck Mini and Original take BMP images.
	- Removed ``width`` and ``height`` information from Deck key image dict, now returned as ``size`` tuple entry.
* 2019-0909: Version 0.4.0 (abcminiuser)
	- Added StreamDeck XL support.
* 2019-0325: Version 0.3.2 (abcminiuser)
	- Fixed StreamDeck Mini key images not updating under some circumstances.
* 2019-0316: Version 0.3.1 (abcminiuser)
	- Added animated image example script.
* 2019-0303: Version 0.3 (abcminiuser)
	- Remapped StreamDeck key indexes so that key 0 is located on the physical
	  top-left of all supported devices.
* 2019-0302: Version 0.2.4 (abcminiuser)
	- Added new ``StreamDeck.get_serial_number()`` function.
	- Added new ``StreamDeck.get_firmware_version()`` function.
* 2019-0223: Version 0.2.3 (abcminiuser)
	- Added new ``StreamDeck.ImageHelpers modules`` for easier key image generation.
