@echo off
REM Initialize _how_to directory from _how_to.example without overwriting existing files

setlocal ENABLEDELAYEDEXPANSION

set "SRC=_how_to.example"
set "DEST=_how_to"

if not exist "%SRC%" (
  echo Source directory "%SRC%" does not exist.
  goto :END
)

if not exist "%DEST%" (
  echo Creating destination directory "%DEST%"...
  mkdir "%DEST%"
)

echo Copying template files from "%SRC%" to "%DEST%" (without overwriting existing files)...

for %%F in ("%SRC%\*") do (
  set "NAME=%%~nxF"
  if not exist "%DEST%\!NAME!" (
    echo   Copying !NAME!
    copy "%%F" "%DEST%\!NAME!" >nul
  ) else (
    echo   Skipping !NAME! (already exists)
  )
)

echo.
echo Initialization finished.

:END
endlocal
pause


