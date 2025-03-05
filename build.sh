#! /bin/bash

rm -rf dist
rm -rf build
rm -rf hypermea_negotiable_auth.egg-info

python setup.py sdist bdist_wheel
