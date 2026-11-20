# API de Usuarios y Libros

API REST hecha con FastAPI que permite gestionar usuarios y libros.
Los datos se guardan en memoria (se reinician al apagar el servidor).

## Requisitos

- Python 3.12

## Instalación

1. Clonar el repositorio:

```bash
git clone <URL-DEL-REPOSITORIO>
cd <NOMBRE-DE-LA-CARPETA>
```

2. Crear y activar un entorno virtual:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Cómo levantar la aplicación

```bash
fastapi dev main.py
```

También se puede usar:

```bash
uvicorn main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000`.

## Documentación interactiva (Swagger)

Con la app corriendo, abrir en el navegador:

**http://127.0.0.1:8000/docs**

