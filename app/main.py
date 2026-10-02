from fastapi import FastAPI
from sqlalchemy import text

from app.config.database import Base, engine
from app.models.requirement import Requirement
from app.routes.requirement_routes import router as requirement_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Requirements API Python",
    description="Microservicio CRUD de requerimientos",
    version="1.0.0",
)


app.include_router(requirement_router)


@app.get("/")
def root():
    return {
        "message": "Requirements API Python funcionando"
    }


@app.get("/test-db")
def test_database():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        return {
            "database": "conectada",
            "result": result.scalar()
        }