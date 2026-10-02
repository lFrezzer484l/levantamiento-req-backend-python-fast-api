# Schemas Pydantic para validar las peticiones y respuestas.
from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class RequirementBase(BaseModel):
    requester: str
    email: EmailStr
    description: str
    requirement_type: str
    priority: str
    titulo: str = "Sin titulo"


class RequirementCreate(RequirementBase):
    pass


class RequirementUpdate(BaseModel):
    requester: str | None = None
    email: EmailStr | None = None
    description: str | None = None
    requirement_type: str | None = None
    priority: str | None = None
    titulo: str | None = None


class RequirementResponse(RequirementBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)