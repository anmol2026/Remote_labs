@echo off

:loop


for /f "tokens=1-3 delims=:." %%A in ("%time%") do (
set m=%%B)


set /p port=< "port.txt"

echo p

if %m% EQU 0 (call npx kill-port %port% -t)
if %m% EQU 29 (call npx kill-port %port% -t)
if %m% EQU 30 (call npx kill-port %port% -t)
if %m% EQU 59 (call npx kill-port %port% -t)

TIMEOUT /T 60

goto loop