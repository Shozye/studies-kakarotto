import base64
import struct


def intarr2long(arr):
    return int(''.join(["%02x" % byte for byte in arr]), 16)


def base64url_to_long(data):
    """
    Stricter then base64_to_long since it really checks that it's
    base64url encoded
    :param data: The base64 string
    :return:
    """
    data = bytes(data, encoding = 'utf-8')
    _d = base64.urlsafe_b64decode(bytes(data) + b'==')
    # verify that it's base64url encoded and not just base64
    # that is no '+' and '/' characters and not trailing "="s.
    if [e for e in [b'+', b'/', b'='] if e in data]:
        raise ValueError("Not base64url encoded")
    return intarr2long(struct.unpack('%sB' % len(_d), _d))
