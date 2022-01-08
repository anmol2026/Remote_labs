@echo off


set /P Board= "Enter Board Number : "
:loop
set /a Board=%Board%
echo %Board%

@REM  setting h as hour, m as minute and d as date
set h=%time:~0,2%
if "%h:~0,1%" == " " set h=0%h:~1,1%

set /a h=1%h%-100
echo %h%

set /a m=%time:~3,2%
if "%m:~0,1%" == " " set m=0%m:~1,1%
set /a m=1%m%-100
echo %m%

set d=%date:~0,2%
if "%d:~0,1%" == " " set d=0%d:~1,1%
set /a d=1%d%-100
echo %d%

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
call E:\Xilinx\Vivado\2019.1\bin\hw_server.bat -s TCP::%port%

@REM adding timeout of 90 seconds
TIMEOUT /T 90

goto loop
