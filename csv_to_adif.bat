echo off
cls
echo Python SOTA Log Converter
echo (C) 2019 K7ASQ
echo *****
set /p callsign="Enter your callsign: "
python csv_to_adif.py %callsign% %*
PAUSE