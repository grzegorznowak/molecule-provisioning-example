#!/bin/bash

sudo apt install virtualenv build-essential python-pip

rm DO_env -rf
virtualenv DO_env --python=python2.7
source DO_env/bin/activate
pip install -r DO-provisioning-requirements.txt
