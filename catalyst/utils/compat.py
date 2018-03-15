from six import PY2
import sys


if PY2:
    from ctypes import py_object, pythonapi

    mappingproxy = pythonapi.PyDictProxy_New
    mappingproxy.argtypes = [py_object]
    mappingproxy.restype = py_object

    def exc_clear():
        sys.exc_clear()

else:
    from types import MappingProxyType as mappingproxy

    def exc_clear():
        # exc_clear was removed in Python 3. The except statement automatically
        # clears the exception.
        pass


try:
    from pandas.core.tools.datetimes import normalize_date
except ImportError:
    from pandas.tslib import normalize_date


unicode = type(u'')

__all__ = [
    'mappingproxy',
    'unicode',
    'normalize_date'
]
