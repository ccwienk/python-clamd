#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

import setuptools


readme = open('README.rst').read()
history = open('CHANGES.rst').read().replace('.. :changelog:', '')

setuptools.setup(
    name='clamd-ccwienk',
    version='1.1.0.dev0',
    author='Christian Cwienk (forked from Thomas Grainger)',
    author_email="see-github-account@github.com",
    maintainer='Christian Cwienk',
    maintainer_email = 'see-github-account@github.com',
    keywords = 'python, clamav, antivirus, scanner, virus, libclamav, clamd',
    description = "Clamd is a python interface to Clamd (Clamav daemon).",
    long_description=readme + '\n\n' + history,
    url='https://github.com/ccwienk/python-clamd',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src', exclude='tests'),
    python_requires='>=3.9.*',
    classifiers = [
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
    zip_safe=True,
    include_package_data=False,
)
