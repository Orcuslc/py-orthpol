#!/usr/bin/env python

from numpy.distutils.core import setup
from numpy.distutils.core import Extension
import os
import glob


setup(name='py-orthpol',
	  version='1.1',
	  description='Construct orthogonal polynomials with respect to arbitrary measures in Python',
	  author='Ilias Bilionis',
	  author_email='ibilion@purdue.edu',
	  maintainer='Chuan Lu',
	  maintainer_email='chuan-lu@uiowa.edu',
	  url='https://github.com/orcuslc/py-orthpol',
	  keywords=['orthogonal polynomails', 'arbitrary probability measures', 'polynomial chaos',
				'generalized polynomial chaos', 'uncertainty quantification'],
	  ext_modules=[Extension('orthpol._orthpol', glob.glob(os.path.join('src', '*.f')))],
	  packages=['orthpol'])
