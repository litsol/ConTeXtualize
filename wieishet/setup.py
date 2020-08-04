# -*- coding: utf-8 -*-
"""\
=======
wieishet
=======

Typeset information from CWI's public accessible people database (PDB).
"""

# FIXME: Please read http://pythonhosted.org/setuptools/setuptools.html to
#        customize in depth your setup script

from setuptools import setup, find_packages
import os, sys

version = '1.0.0.dev0'

this_directory = os.path.abspath(os.path.dirname(__file__))

def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.rst',),('CHANGES.rst',))]
    )
dev_require = []
if sys.version_info < (2, 7):
    dev_require += ['unittest2']


setup(name='wieishet',
      version=version,
      description="Typeset information from CWI's public accessible people database (PDB).",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
          ],
      keywords='',  # FIXME: Add whatefer fits
      author='A.E. van Aggelen',
      author_email='A.E.van.Aggelen@cwi.nl',
      url='http://pypi.python.org/pypi/wieishet',
      license='GPLv3',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # 3rd party
          'setuptools'
          # Others
          ],
      entry_points={
          'console_scripts': ['wieishet=wieishet.__main__:main']
          },
      tests_require=dev_require,
      test_suite='tests.all_tests',
      extras_require={
          'dev': dev_require
      })
