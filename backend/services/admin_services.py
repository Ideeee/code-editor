from sqlalchemy.orm import Session

import bcrypt

from schemas import admin_schemas
from models import admin_model


def get_admin(db: Session, admin_id: int):
    return db.query(admin_model.Admin).filter(admin_model.Admin.id == admin_id).first()


def get_admin_by_username(db: Session, username: str):
    return db.query(admin_model.Admin).filter(admin_model.Admin.username == username).first()


def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(admin_model.Admin).offset(skip).limit(limit).all()


def create_admin(db: Session, admin: admin_schemas.AdminCreate):
    hashed_password = admin_model.Admin.make_password_hash(admin.password)
    
    new_admin = admin_model.Admin(
        username=admin.username, 
        password_hash=hashed_password,
        role=admin.role, 
        first_name=admin.first_name, 
        last_name=admin.last_name, 
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return admin_schemas.Admin.from_orm(new_admin)


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(admin_model.Item).offset(skip).limit(limit).all()


# def create_admin_item(db: Session, item: schemas.ItemCreate, admin_id: int):
#     db_item = admin_model.Item(**item.dict(), owner_id=admin_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


