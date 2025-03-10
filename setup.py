#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='hypermea-negotiable-auth',
    version='0.9.7',
    description='Hypermea negotiable authentication',
    long_description= open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    author='Michael Ottoson',
    author_email='michael@pointw.com',
    url='https://github.com/pointw-dev/hypermea-negotiable-auth',
    keywords=['hypermea', 'eve', 'api', 'rest', 'auth', 'http'],
    packages=find_packages(),
    license='MIT',
    install_requires=['eve>=0.8.0', 'authparser>=1.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Security',
    ]
)
