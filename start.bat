@echo off
cd /d D:\aplicaciones\pc-isla

:: Activar entorno virtual
call env\Scripts\activate.bat

:: Actualizar código desde GitHub
git pull origin main

:: Instalar dependencias Python nuevas
pip install -r requirements.txt

:: Migraciones de base de datos
python manage.py migrate --noinput

:: Recopilar estáticos de Django
python manage.py collectstatic --noinput

:: Build del frontend React
call npm run build

:: Levantar Django con Waitress
python serve.py
