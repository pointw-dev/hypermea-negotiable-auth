#!/bin/bash

rm -rf dist
rm -rf build
rm -rf hypermea_negotiable_auth.egg-info

python setup.py sdist bdist_wheel

echo
echo ----------
echo publish to test: twine upload --repository-url https://test.pypi.org/legacy/ dist/*
echo publish to prod: twine upload/*
echo ----------
