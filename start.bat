@echo off
:loop

set /a Board = 1

@REM  setting h as hour, m as minute and d as date
set /a h=%time:~0,2%
if "%h:~0,1%" == " " set /a h=0%h:~1,1%
echo %h%
set /a m=%time:~3,2%
if "%m:~0,1%" == " " set /a m=0%m:~1,1%

set /a d=%date:~0,2%
if "%d:~0,1%" == " " set /a d=0%d:~1,1%

@REM getting current slot id
set /a slot = %h% * 100
if %m% LSS 30 (set /a slot = %slot%) else (set /a slot = %slot% + 30)
echo %h%
echo %slot%

@REM calling arduino.py to resart board
call python arduino.py 

@REM calling ssh_call.py to establish connection between SSH VM and run scripts on it 
call python ssh_call.py %Board% %slot%

@REM reading port number from port.txt file
set /p port=< "port.txt"

@REM Esablishing hw_server with random port
call D:\Xilinx\Vivado\2019.1\bin\hw_server.bat -s TCP::%port%

@REM adding timeout of 90 seconds
TIMEOUT /T 90

goto loop
