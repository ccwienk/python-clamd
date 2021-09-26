clamd
=====


About
-----

`clamd` is a Python module to use the ClamAV anti-virus engine programmatically
from Python code. It requires a running instance of the `clamd` daemon.

This is a fork (with friendly intention) of `clamd` from https://github.com/graingert/python-clamd,
which itself has been forked (see README there).

This fork intends to:

- add some more convenience (e.g. auto-detect socket-path)
- rm legacies (e.g. support for Python2.x)
- add async interface

Note that I do not care at all about Windows/NT or Darwin/XNU, so it is very likely that
some or all features will break in future versions of this module.

Usage
-----

To use with a unix socket::

    >>> import clamd
    >>> cd = clamd.ClamdUnixSocket()
    >>> cd.ping()
    'PONG'
    >>> cd.version()                             # doctest: +ELLIPSIS
    'ClamAV ...
    >>> cd.reload()
    'RELOADING'

To scan a file::

    >>> open('/tmp/EICAR','wb').write(clamd.EICAR)
    >>> cd.scan('/tmp/EICAR')
    {'/tmp/EICAR': ('FOUND', 'Eicar-Test-Signature')}

To scan a stream::

    >>> from io import BytesIO
    >>> cd.instream(BytesIO(clamd.EICAR))
    {'stream': ('FOUND', 'Eicar-Test-Signature')}


License
-------
`clamd` is released as open-source software under the LGPL license.
