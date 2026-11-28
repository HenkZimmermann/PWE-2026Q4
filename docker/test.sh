#!/bin/bash
set -e

cd ../backend
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-test.txt
.venv/bin/python -m pytest
