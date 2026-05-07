# Portal AIET

Aplicación web full-stack compuesta por un backend en **Django** (API REST) y un frontend en **React**.

---

## Requisitos previos

- Python 3.10+
- Node.js 18+ y npm
- Git

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/rodrigo-coco-espinoza/pc-isla.git
cd pc-isla
```

### 2. Backend (Django)

#### 2.1 Crear y activar el entorno virtual

```bash
python -m venv env
```

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
source env/bin/activate
```

#### 2.2 Instalar dependencias Python

```bash
pip install -r requirements.txt
```

#### 2.3 Configurar variables de entorno del backend

Copia el archivo de ejemplo y edítalo con tus valores:

```bash
cp core/.env.example core/.env
```

Edita `core/.env` y ajusta al menos las siguientes variables:

| Variable | Descripción |
|---|---|
| `SECRET_KEY` | Clave secreta de Django (debe ser única y segura en producción) |
| `DEBUG` | `True` en desarrollo, `False` en producción |
| `DATABASE_URL` | Ruta absoluta al archivo SQLite, p. ej. `C:\ruta\al\proyecto\db.sqlite3` |
| `MEDIA_ROOT` | Ruta absoluta a la carpeta `media/`, p. ej. `C:\ruta\al\proyecto\media` |
| `ALLOWED_HOST_DEV` | Host(s) permitidos en desarrollo, p. ej. `*` |
| `CORS_ORIGIN_WHITELIST_DEV` | Origen del frontend, p. ej. `http://localhost:3000` |
| `CSRF_TRUSTED_ORIGIN_DEV` | Mismo origen que CORS, p. ej. `http://localhost:3000` |

#### 2.4 Aplicar migraciones

```bash
python manage.py migrate
```

#### 2.5 Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

---

### 3. Frontend (React)

#### 3.1 Instalar dependencias Node

```bash
npm install
```

#### 3.2 Configurar variables de entorno del frontend

Copia el archivo de ejemplo y edítalo:

```bash
cp .env.example .env
```

Edita `.env`:

| Variable | Descripción |
|---|---|
| `REACT_APP_API_URL` | URL base del backend, p. ej. `http://localhost:8000` |

---

## Ejecución en desarrollo

Abre dos terminales en la raíz del proyecto.

### Terminal 1 — Backend

```bash
# Con el entorno virtual activado
python manage.py runserver
```

El backend estará disponible en `http://localhost:8000`.

### Terminal 2 — Frontend

```bash
npm start
```

El frontend estará disponible en `http://localhost:3000`.

---

## Estructura del proyecto

```
portal-aiet/
├── apps/               # Aplicaciones Django
│   ├── base/
│   ├── buscador/
│   ├── informes/
│   ├── pc_isla/
│   └── user/
├── core/               # Configuración Django (settings, urls, .env)
├── src/                # Código fuente React
├── public/             # Archivos estáticos públicos de React
├── media/              # Archivos subidos por los usuarios (generado)
├── manage.py
├── requirements.txt
└── package.json
```

---

## Panel de administración

Una vez ejecutado el backend, el panel de administración de Django está disponible en:

```
http://localhost:8000/admin/
```
