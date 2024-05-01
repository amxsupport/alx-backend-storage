#!/usr/bin/env python3
""" Redis module. """

from functools import wraps
import redis
import sys
from typing import Union, Optional, Callable
from uuid import uuid4


def replay(method: Callable):
    """ Replay. """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])
    count = method.__self__.get(key)
    i_list = method.__self__._redis.lrange(i, 0, -1)
    o_list = method.__self__._redis.lrange(o, 0, -1)
    queue = list(zip(i_list, o_list))
    print(f"{key} was called {decode_utf8(count)} times:")
    for k, v, in queue:
        k = decode_utf8(k)
        v = decode_utf8(v)
        print(f"{key}(*{k}) -> {v}")


