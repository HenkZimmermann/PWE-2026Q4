@echo off
setlocal

cd /d "..\backend"
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-test.txt
.venv\Scripts\python.exe -m pytest
