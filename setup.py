
from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import EcxAnx
import tests

here = os.path.abspath(os.path.dirname(__file__))

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
   name='EcxAnx',
   version='1.0',
   description='Econometrics and analytics for time series.',
   license='MIT',
   author='Luis Huesca Molina',
   author_email='katakrask@gmail.com',
   packages=['EcxAnx'],
   install_requires=['numpy', 'pandas'],
)