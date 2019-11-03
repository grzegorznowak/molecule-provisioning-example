#!/bin/bash

sudo apt install virtualenv build-essential python3-pip

rm provisioningenv -rf
virtualenv provisioningenv --python=python3.6
. provisioningenv/bin/activate
pip install -r provisioning-requirements.txt
