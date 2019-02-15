dump_xml
========

.. image:: https://img.shields.io/pypi/v/dump_xml.svg
    :target: https://pypi.python.org/pypi/dump_xml
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/intouch-smartwater/dump_xml.png
   :target: https://travis-ci.org/intouch-smartwater/dump_xml
   :alt: Latest Travis CI build status

.. image:: https://img.shields.io/pypi/l/dump_xml.svg
    :target: https://pypi.python.org/pypi/dump_xml
    :alt: License

.. image:: https://img.shields.io/pypi/pyversions/dump_xml.svg
    :target: https://pypi.python.org/pypi/dump_xml
    :alt: Support Python Versions

A simple dictionary to XML converter that "Just Works".

Usage
-----
.. code:: python

  $ python
  >>> from dump_xml import dump_xml
  >>> dump_xml({1: 2}, name="root")
  <Element 'root' at 0x0000000003B104A8>

Installation
------------

.. code:: bash

  $ pip install dump_xml

Compatibility
-------------

Tests run on Python 2.7 and 3.4 - 3.7. Compatibility is aimed primarily at
ensuring 3.x as a first-class experience, with 2.x as a "nice-to-have".

Licence
-------

MIT

Authors
-------

`dump_xml` was written by `James Cheese <james.cheese@intouch-ltd.com>`_.
