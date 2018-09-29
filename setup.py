from setuptools import setup, find_packages
# To use a consistent encoding
# from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='wordcounter',
    version='0.0.2.2',
    description='A simple Python module to count words in your given text and many more',
    long_description=open('README.rst').read(),
    # The project's main homepage.
    url='https://github.com/OmkarPathak/Word-Counter',
    # Author details
    author='Omkar Pathak',
    author_email='omkarpathak27@gmail.com',
    # Choose your license
    license='GPL-2.0',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages()
)