#!/usr/bin/python2

from setuptools import setup, find_packages

setup(
    name = 'pygments-style-railscasts',
    version = '0.2',
    description = 'Pygments version of the "railscasts" vim theme.',
    license = 'BSD',

    author = 'Marcus Fredriksson',
    author_email = 'drmegahertz@gmail.com',

    url = 'https://github.com/DrMegahertz/pygments-style-railscasts',

    packages = ['pygments_style_railscasts'],
    install_requires = ['pygments >= 1.4'],

    entry_points = '''[pygments.styles]
                      railscasts = pygments_style_railscasts:RailscastsStyle''',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
