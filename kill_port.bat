@echo off

:loop

@REM setting variable m as current time(minutes)  
for /f "tokens=1-3 delims=:." %%A in ("%time%") do (
set m=%%B)

@REM Reading port from text file
set /p port=< "port.txt"
echo %m%

@REM killing port if m equal 0, 29, 30 or 59
if %m% EQU 0 (call npx kill-port %port% -t)
if %m% EQU 29 (call npx kill-port %port% -t)
if %m% EQU 30 (call npx kill-port %port% -t)
if %m% EQU 59 (call npx kill-port %port% -t)

@REM adding wait of 60 seconds
TIMEOUT /T 60

goto loop