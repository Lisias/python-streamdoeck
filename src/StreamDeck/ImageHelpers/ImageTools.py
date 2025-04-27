#         Python Stream Doeck Library
#      Released under the GPLv2 licence
#
#  Authors:
#    * Lisias T (https://github.com/lisias)

import os

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "../..", "Assets")

def load_asset(fname:str) -> list:
    fullpathname = os.path.join(ASSETS_PATH, fname)
    with open(fullpathname, mode='rb') as f:
        payload = f.read()
    return payload

