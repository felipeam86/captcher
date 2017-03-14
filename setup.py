#!/usr/bin/env python

import os

try:
    from setuptools import setup
except:
    from distutils.core import setup  # noqa

extra = {}
try:
    from Cython.Build import cythonize
    p = os.path.join('captcher')
    extra['ext_modules'] = cythonize(
        [os.path.join(p, '*.py')],
        exclude=os.path.join(p, '__init__.py'),
        nthreads=2, quiet=True)
except ImportError:
    pass

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

install_requires = [
]

try:
    import uuid  # noqa
except ImportError:
    install_requires.append('uuid')

setup(
    name='captcher',
    version='0.1',
    description='A lightweight captcher library',
    long_description=README,
    url='https://github.com/felipeam86/captcher',

    author='Andriy Kornatskyy',
    author_email='andriy.kornatskyy at live.com',

    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='wsgi http captcher',
    packages=['captcher'],

    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'PIL': [
            'PIL'
        ],
        'Pillow': [
            'Pillow'
        ],
        'dev': [
            'coverage',
            'nose',
            'pytest',
            'pytest-pep8',
            'pytest-cov',
        ],
    },

    platforms='any',
    **extra
)
