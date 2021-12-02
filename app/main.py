from typing import List
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.orm import Session
from crud import crud

from models import models

from schemas import schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=Page[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return paginate(users)

@app.get("/users/", response_model=Page[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return paginate(users)


add_pagination(app)


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.User, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user=user, user_id=user_id)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user_id=user_id)


@app.get('/')
def index():
    return {'data': 'success'}
