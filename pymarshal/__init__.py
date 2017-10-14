"""
    Replicates the functionality of Golang's
    struct (un)marshalling feature to/from JSON.

    For examples, see:
    https://github.com/j3ffhubb/pymarshal/blob/master/README.rst
"""

from .json import *
from .type import *

__all__ = [
    'marshal_json',
    'type_assert',
    'type_assert_iter',
    'unmarshal_json',
]