
from setuptools import setup

__version__ = 0, 3, 0
__version_string__ = '.'.join(str(x) for x in __version__)

__author__ = 'Doug Napoleone, Samuel Marks, Eric Frederich'
__email__ = 'doug.napoleone+plantuml@gmail.com'

setup(
    name='plantuml',
    version=__version_string__,
    description='',
    long_description=open('README.md', 'r').read(),
    url='https://github.com/dougn/python-plantuml/',
    author=__author__,
    author_email=__email__,
    license='BSD',
    py_modules=['plantuml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['httplib2'],
    keywords=['plantuml', 'uml']
)
