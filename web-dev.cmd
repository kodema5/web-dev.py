@echo off
setlocal
set SCRIPT_DIR=%~dp0
set PIPENV_PIPFILE=%SCRIPT_DIR%Pipfile
python3 -m pipenv run python3 %SCRIPT_DIR%\main.py %*
endlocal