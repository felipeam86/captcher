
Getting Started
===============

Install
-------

:ref:`captcher` requires `python`_ version 2.4 to 2.7 or 3.2+.
It is operating system independent. You can install it from the `pypi`_
site using `setuptools`_ (you need to specify an extra requirements per
the imaging library of your choice)::

    $ easy_install captcher
    $ easy_install captcher[PIL]
    $ easy_install captcher[Pillow]

If you are using `virtualenv`_::

    $ virtualenv env
    $ env/bin/easy_install captcher

Develop
-------

You can get the `source code`_ using `git`_::

    $ git clone https://github.com/felipeam86/captcher
    $ cd captcher

Prepare `virtualenv`_ environment in *env* directory ::

    $ make env

... and run all tests::

    $ make test

You can read how to compile from source code different versions of
`python`_ in the `article`_ published on `mind reference`_ blog.

You can run certain make targets with a specific python version. Here
we are going to run `doctest`_ with python3.2::

    $ make env doctest-cover VERSION=3.2

Generate documentation with `sphinx`_::

	$ make doc

If you run into any issue or have comments, go ahead and add on
`bitbucket`_.

.. _`pypi`: http://pypi.python.org/pypi/wheezy.captcha
.. _`python`: http://www.python.org
.. _`setuptools`: http://pypi.python.org/pypi/setuptools
.. _`bitbucket`: http://bitbucket.org/akorn/wheezy.captcha/issues
.. _`source code`: http://bitbucket.org/akorn/wheezy.captcha/src
.. _`mercurial`: http://mercurial.selenic.com/
.. _`virtualenv`: http://pypi.python.org/pypi/virtualenv
.. _`article`: http://mindref.blogspot.com/2011/09/compile-python-from-source.html
.. _`mind reference`: http://mindref.blogspot.com/
.. _`doctest`: http://docs.python.org/library/doctest.html
.. _`sphinx`: http://sphinx.pocoo.org/
