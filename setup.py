#! /usr/bin/env python3

import sys

try:
    from setuptools import setup
except ImportError:
        print("Missing package setuptoolsx. Please install to continue\n(https://pypi.python.org/pypi/setuptools)")
        sys.exit('Exiting now!!')

DESCRIPTION = 'Command-line torrent search program for Windows, Linux and  MacOS'
LONG_DESCRIPTION = 'Please visit https://github.com/kryptxy/torrench for docs.'
VERSION = '1.0.61'

setup(
    name="torrench",
    version=VERSION,
    author="kryptxy",
    author_email="kryptxy@protonmail.com",
    description=(DESCRIPTION),
    license="GPL",
    url="https://github.com/kryptxy/torrench",
    packages=['torrench', 'torrench.modules','torrench.utilities'],
    install_requires=['beautifulsoup4','lxml','requests','tabulate','colorama', 'pyperclip'],
    long_description=(LONG_DESCRIPTION),
    entry_points={'console_scripts': ['torrench = torrench.__main__:main']},
    zip_safe=False,
    keywords=['torrents', 'distrowatch', 'linuxtracker', 'linux', 'windows', 'cli', 'terminal'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities",
    ],
)
