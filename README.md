# Requirements API Python

Microservicio CRUD de requerimientos desarrollado con FastAPI.

## Estructura

- `app/main.py`: punto de entrada de FastAPI.
- `app/config/`: configuración y conexión a base de datos.
- `app/models/`: modelos SQLAlchemy.
- `app/schemas/`: schemas Pydantic.
- `app/repositories/`: acceso a datos.
- `app/services/`: lógica de negocio.
- `app/routes/`: endpoints de la API.

## Ejecutar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```
