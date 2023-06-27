from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import re


def send(keys_str: str):
    keys = []
    if matches := re.findall(r'{(\w+)}', keys_str):
        for match in matches:
            keys.append(match[0].upper())
    else:
        keys = [x for x in keys_str]

    for key in keys:
        press(key)
