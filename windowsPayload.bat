:: Locate absolute path to the Payload directory using this file location
SET PAYLOAD_DIR=%~dp0

:: So we can now use relative paths
cd %PAYLOAD_DIR%

::start reciever
START "reciever.py" python3 reciever.py

::delay one second so reciever has time to clear old coords.txt
TIMEOUT 1

START "writer.py" python3 writer.py