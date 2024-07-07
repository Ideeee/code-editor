import fastapi
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from services import admin_services
from models import admin_model
from schemas import admin_schemas
from db.db_setup import SessionLocal, engine, get_db


router = fastapi.APIRouter(tags=["Admin"])

@router.post("/admin/", response_model=admin_schemas.Admin)
def create_admin(
    admin: admin_schemas.AdminCreate, 
    db: Session = Depends(get_db)
    ):

    # existing_admin = admin_services.get_admin_by_username(db, username=admin.username)
    # if existing_admin:
    #     raise HTTPException(status_code=400, detail="A user with this username already exists")
    
    try:
        new_admin = admin_services.create_admin(db=db, admin=admin)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="A user with this username already exists")
    except:
        raise HTTPException(status_code=400, detail="Could not create admin. Check parameters")

    
    return new_admin

@router.post("/admin/login", status_code=200, response_model=admin_schemas.Admin)
async def login(
    admin: admin_schemas.AdminLogin, 
    db: Session = Depends(get_db)
):
    verified_admin = admin_services.get_admin_by_username(db=db, username=admin.username)

    if verified_admin is None:
        raise fastapi.HTTPException(status_code=403, detail="Invalid Credentials")
    
    # password_bytes = admin.password.encode()
    verified = verified_admin.check_password(admin.password)

    if not verified:
        raise fastapi.HTTPException(status_code=403, detail="Invalid Credentials")
    
    return verified_admin