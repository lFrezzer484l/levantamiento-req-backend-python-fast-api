from sqlalchemy.orm import Session

from app.repositories.requirement_repository import RequirementRepository
from app.schemas.requirement import RequirementCreate, RequirementUpdate


class RequirementService:

    @staticmethod
    def get_all(db: Session):
        return RequirementRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db: Session,
        requirement_id: int
    ):
        return RequirementRepository.get_by_id(
            db,
            requirement_id
        )

    @staticmethod
    def create(
        db: Session,
        requirement_data: RequirementCreate
    ):
        return RequirementRepository.create(
            db,
            requirement_data
        )

    @staticmethod
    def update(
        db: Session,
        requirement_id: int,
        requirement_data: RequirementUpdate
    ):
        requirement = RequirementRepository.get_by_id(
            db,
            requirement_id
        )

        if not requirement:
            return None

        return RequirementRepository.update(
            db,
            requirement,
            requirement_data
        )

    @staticmethod
    def delete(
        db: Session,
        requirement_id: int
    ):
        requirement = RequirementRepository.get_by_id(
            db,
            requirement_id
        )

        if not requirement:
            return False

        RequirementRepository.delete(
            db,
            requirement
        )

        return True