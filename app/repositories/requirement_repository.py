from sqlalchemy.orm import Session

from app.models.requirement import Requirement
from app.schemas.requirement import RequirementCreate, RequirementUpdate


class RequirementRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Requirement).all()

    @staticmethod
    def get_by_id(db: Session, requirement_id: int):
        return (
            db.query(Requirement)
            .filter(Requirement.id == requirement_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        requirement_data: RequirementCreate
    ):
        requirement = Requirement(
            requester=requirement_data.requester,
            email=requirement_data.email,
            description=requirement_data.description,
            requirement_type=requirement_data.requirement_type,
            priority=requirement_data.priority,
            titulo=requirement_data.titulo
        )

        db.add(requirement)
        db.commit()
        db.refresh(requirement)

        return requirement

    @staticmethod
    def update(
        db: Session,
        requirement: Requirement,
        requirement_data: RequirementUpdate
    ):
        update_data = requirement_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(requirement, field, value)

        db.commit()
        db.refresh(requirement)

        return requirement

    @staticmethod
    def delete(
        db: Session,
        requirement: Requirement
    ):
        db.delete(requirement)
        db.commit()