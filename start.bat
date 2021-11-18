@echo off
:loop

set /a Board = 1
set /a tt =0

set /a h=%time:~0,2%
if "%h:~0,1%" == " " set /a h=0%h:~1,1%
echo %h%
set /a m=%time:~3,2%
if "%m:~0,1%" == " " set /a m=0%m:~1,1%

set /a d=%date:~0,2%
if "%d:~0,1%" == " " set /a d=0%d:~1,1%

set /a slot = %h% * 100

if %m% LSS 30 (set /a slot = %slot%) else (set /a slot = %slot% + 30)
echo %h%
echo %slot%

call python arduino.py %tt%
call python ssh_call.py %Board% %slot%
@REM call python spreadsheet.py %Board% %slot%

set /p port=< "port.txt"

@REM call gmail.py
@REM call python ssh_call.py %Board% %slot%
call E:\Xilinx\Vivado\2019.1\bin\hw_server.bat -s TCP::%port%
TIMEOUT /T 90

goto loop
