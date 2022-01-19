@ECHO OFF
pip install pyinstaller
pyinstaller ../main.py --onefile --noconsole --distpath build/ --icon="ICO/favicon.ico"
del main.spec
cd "build"
rmdir "main" /S /Q
cd ../../
rmdir "__pycache__" /S /Q
exit