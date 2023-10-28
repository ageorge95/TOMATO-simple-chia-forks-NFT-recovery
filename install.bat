@echo off

:: installation

git submodule update --progress --init --recursive --force

python -m venv venv
:: Windows doesn't allow the creation of symlinks without special priviledges, so hardlinks are created instead.
mklink /h activate.bat venv\Scripts\activate.bat
mklink /j venv\Scripts\chia chia_blockchain\chia
mklink /j venv\Scripts\basket basket

call activate.bat

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python setup.py install

:: post-installation message

echo @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
echo.
echo TOMATO install complete.
echo Join the Discord server for support: https://discord.gg/5HeFcrVFJZ
echo.
echo Run 'activate' to activate TOMATO's Python virtual environment and
echo 'deactivate' to, well, deactivate it.
echo.
echo Run 'tomato -h' for further instructions.
echo.
echo @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

pause

deactivate