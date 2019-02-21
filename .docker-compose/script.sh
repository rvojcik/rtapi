#!/bin/sh

pip install -r requirements.txt
python setup.py install
pip install -r tests/requirements.txt
coverage run --source rtapi -m py.test
coverage report