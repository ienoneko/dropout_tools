"""Provide some missing bits in the `os' package, Linux-specific."""
from ctypes import CDLL, c_char_p, c_int, c_ulong, c_void_p, get_errno
from os import strerror

MS_BIND = 4096
MS_REC = 16384

_libc = CDLL('libc.so.6', use_errno=True)

def _nonzero_is_err(res, f, args):
  if res != 0:
    err = get_errno()
    raise OSError(err, strerror(err))

_mount = _libc.mount
_mount.argtypes = [ c_char_p, c_char_p, c_char_p, c_ulong, c_void_p ]
_mount.restype = c_int
_mount.errcheck = _nonzero_is_err

def _try_enc(s):
  if s is not None:
    return s.encode()

def mount(src, tgt, fs, fl, d):
  # According to manpage,
  # `src' and `fs' are ignored when remounting,
  # `fs' and `d' are ignored for "bind mount"s.
  # The caller may then pass nullptr (i.e. None) for these.
  _mount(_try_enc(src), tgt.encode(), _try_enc(fs), fl, _try_enc(d))
