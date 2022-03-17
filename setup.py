#!/usr/bin/env python3

try:
    from setuptools import setup, find_packages

except ImportError:
    from distutils.core import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='wgnsite',
    packages=find_packages(),
    version='0.0.5',
    url='https://madewgn.my.id',
    description='Simple SSG written in Python.',
    long_description=read_md('README.md'),
    long_description_content_type="text/markdown",
    author='Made Wiguna',
    author_email='madewgn2@gmail.com',
    license='MIT',
    scripts=['wgnsite'],
    install_requires=[
        'requests',
        'jinja2',
        'markdown2',
        'docopt'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ]
)
