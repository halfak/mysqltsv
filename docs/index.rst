MySQL TSV Processing!
=====================
This library provides functionality for reading and producing MySQL compatible
Tab-Seperated Value files.  The most salient features of this library are
the :class:`~mysqltsv.reader.Reader` and :class:`~mysqltsv.writer.Writer` that
enable reading and writing TSV files.  There's also a set of convenience
functions for doing the same without constructing a class -- see :func:`~mysqltsv.functions.read` and :func:`~mysqltsv.functions.write`.


Contents
--------
.. toctree::
    :maxdepth: 2

    reading
    writing
    errors

Reading and Writing
-------------------

Use :class:`~mysqltsv.reader.Reader` or :func:`~mysqltsv.functions.read` to
read TSV files:

  >>> import io
  >>> my_file = io.StringIO("user_id\tuser_text\tedits\n" +
  ...                       "10\tFoobar_Barman\t2344\n" +
  ...                       "11\tBarfoo_Fooman\t20\n" +
  ...                       "NULL\t127.0.0.1\t42\n")
  >>> reader = mysqltsv.Reader(my_file, types=[int, str, int])
  >>> for row in reader:
  ...     print(repr(row.user_id), repr(row['user_text']), repr(row[2]))
  ...
  10 'Foobar_Barman' 2344
  11 'Barfoo_Fooman' 20
  None '127.0.0.1' 42

Use :class:`~mysqltsv.writer.Writer` or :func:`~mysqltsv.functions.write` to write TSV files:

  >>> import sys
  >>> import mysqltsv
  >>>
  >>> writer = mysqltsv.Writer(sys.stdout, headers=['user_id', 'user_text', 'edits'])
  user_id	user_text	edits
  >>> writer.write([10, 'Foobar_Barman', 2344])
  10	Foobar_Barman	2344
  >>> writer.write({'user_text': 'Barfoo_Fooman', 'user_id': 11, 'edits': 20})
  11	Barfoo_Fooman	20
  >>> writer.write([None, "127.0.0.1", 42])
  NULL	127.0.0.1	42

Authors
-------
* Aaron Halfaker https://github.com/halfak

.. code::

  MIT LICENSE

  Copyright (c) 2015 Aaron Halfaker <aaron.halfaker@gmail.com>

  Permission is hereby granted, free of charge, to any person
  obtaining a copy of this software and associated documentation
  files (the "Software"), to deal in the Software without
  restriction, including without limitation the rights to use,
  copy, modify, merge, publish, distribute, sublicense, and/or
  sell copies of the Software, and to permit persons to whom
  the Software is furnished to do so, subject to the following
  conditions:

  The above copyright notice and this permission notice shall
  be included in all copies or substantial portions of the
  Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
  KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
  PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
  OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
