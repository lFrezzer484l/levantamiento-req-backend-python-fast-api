from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.requirement import (
    RequirementCreate,
    RequirementResponse,
    RequirementUpdate,
)
from app.services.requirement_service import RequirementService


router = APIRouter(
    prefix="/api/requirements",
    tags=["Requirements"]
)


@router.get(
    "",
    response_model=list[RequirementResponse]
)
def get_requirements(
    db: Session = Depends(get_db)
):
    return RequirementService.get_all(db)


@router.get(
    "/{requirement_id}",
    response_model=RequirementResponse
)
def get_requirement(
    requirement_id: int,
    db: Session = Depends(get_db)
):
    requirement = RequirementService.get_by_id(
        db,
        requirement_id
    )

    if not requirement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requirement no encontrado"
        )

    return requirement


@router.post(
    "/create",
    response_model=RequirementResponse,
    status_code=status.HTTP_201_CREATED
)
def create_requirement(
    requirement_data: RequirementCreate,
    db: Session = Depends(get_db)
):
    return RequirementService.create(
        db,
        requirement_data
    )


@router.put(
    "/{requirement_id}",
    response_model=RequirementResponse
)
def update_requirement(
    requirement_id: int,
    requirement_data: RequirementUpdate,
    db: Session = Depends(get_db)
):
    requirement = RequirementService.update(
        db,
        requirement_id,
        requirement_data
    )

    if not requirement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requirement no encontrado"
        )

    return requirement


@router.delete(
    "/{requirement_id}",
    status_code=status.HTTP_200_OK
)
def delete_requirement(
    requirement_id: int,
    db: Session = Depends(get_db)
):
    deleted = RequirementService.delete(
        db,
        requirement_id
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requirement no encontrado"
        )
    
    return {
        "message": "Requirement eliminado correctamente"
    }