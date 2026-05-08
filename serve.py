import os
from waitress import serve
from core.wsgi import application

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8088))
    host = os.environ.get('HOST', '0.0.0.0')
    print(f'Iniciando servidor en http://{host}:{port}')
    serve(application, host=host, port=port, threads=4)
