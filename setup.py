#!/usr/bin/env python

import os
from setuptools import find_packages, setup

install_requires = [
    line.rstrip() for line in open(
      os.path.join(os.path.dirname(__file__), "REQUIREMENTS.txt")
    )
]

setup(name='TravisTest',
      install_requires=install_requires,
      version='0.0.1',
      description='Testing travis',
      url='https://github.com/kevinyamauchi/TravisTest',
      author='Kevin Yamauchi',
      author_email='kevin.yamauchi@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
