`captcher`_ is a `python`_ package written in pure Python
code. It is a lightweight captcha library that provides integration
with (one of below must be installed):

* `PIL`_ - Python Imaging Library 1.1.7.
* `Pillow`_ - Python Imaging Library (fork).

It is optimized for performance, well tested and documented.

Resources:

* `source code`_, `examples`_ and `issues`_ tracker are available
  on `bitbucket`_
* `documentation`_, `readthedocs`_
* `eggs`_ on `pypi`_

Install
-------

`captcher`_ requires `python`_ version 2.4 to 2.7 or 3.2+.
It is independent of operating system. You can install it from `pypi`_
site using `setuptools`_ (you need specify extra requirements per
imaging library of your choice)::

    $ easy_install captcher
    $ easy_install captcher[PIL]
    $ easy_install captcher[Pillow]

If you are using `virtualenv`_::

    $ virtualenv env
    $ env/bin/easy_install captcher

If you run into any issue or have comments, go ahead and add on
`bitbucket`_.

