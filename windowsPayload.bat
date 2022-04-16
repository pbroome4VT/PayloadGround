:: Locate absolute path to the Payload directory using this file location
SET PAYLOAD_DIR=%~dp0

:: So we can now use relative paths
cd %PAYLOAD_DIR%

START "reciever.py" python3 reciever.py
START "writer.py" python3 writer.py