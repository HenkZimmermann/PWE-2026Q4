@echo off
setlocal

cd /d "..\backend"
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-test.txt
.venv\Scripts\python.exe -m pytest
