@echo off
setlocal
set SCRIPT_DIR=%~dp0
set PIPENV_PIPFILE=%SCRIPT_DIR%Pipfile
pipenv run python %SCRIPT_DIR%\main.py %*
endlocal