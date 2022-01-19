pip install pyinstaller
pyinstaller ../main.py --onefile --noconsole --distpath build/ --icon="ICO/favicon.ico"
rm main.spec
rm -rfv build/main
rm -rfv ../__pycache__
exit