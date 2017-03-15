`captcher`_ is a package written in pure Python
code. It is a lightweight captcha library that provides integration
with (one of below must be installed):

* `PIL`_ - Python Imaging Library 1.1.7.
* `Pillow`_ - Python Imaging Library (fork).

It is friendly a fork of `wheezy.captcha`_, mostly for personal purposes. Source code and examples are available  on `github`_

Install
-------

`captcher`_ requires version 2.4 to 2.7 or 3.2+.
It is independent of operating system. You can install it from `pypi`_
site using `setuptools`_ (you need specify extra requirements per
imaging library of your choice)::

    $ git clone https://github.com/felipeam86/captcher
    $ cd captcher/
    $ python setup.py install

If you run into any issue or have comments, go ahead and add on
`github`_.

.. _`github`: https://github.com/felipeam86/captcher
.. _`doctest`: http://docs.python.org/library/doctest.html
.. _`eggs`: http://pypi.python.org/pypi/wheezy.captcha
.. _`pil`: http://www.pythonware.com/products/pil/
.. _`pillow`: https://pypi.python.org/pypi/Pillow
.. _`pypi`: http://pypi.python.org
.. _`setuptools`: http://pypi.python.org/pypi/setuptools
.. _`source code`: https://github.com/felipeam86/captcher
.. _`virtualenv`: http://pypi.python.org/pypi/virtualenv
.. _`captcher`: http://pypi.python.org/pypi/captcher
.. _`wheezy.captcha`: http://pypi.python.org/pypi/wheezy.captcha