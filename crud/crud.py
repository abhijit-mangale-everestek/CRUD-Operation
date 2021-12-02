from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from crud_logger import logger


def create_user(db: Session, user: schemas.User):
    try:
        db_user = models.User(first_name=user.first_name, last_name=user.last_name, gender=user.gender)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info('User Created --> Name: {} {} Gender:{}'.format(user.first_name, user.last_name, user.gender))
        return db_user
    except Exception as e:
        logger.exception('Got exception -->> '.format(e))


def get_users(db: Session, skip: int = 0, limit: int = 100):
    try:
        tablecontainsrecordsornot = db.query(models.User).first()
        if tablecontainsrecordsornot is not None:
            logger.info('Successfully fetched List of users')
            return db.query(models.User).offset(skip).limit(limit).all()
        else:
            logger.warning('Database is Empty create user first')
    except Exception as e:
        logger.exception('Got exception -->> '.format(e))


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_user(db: Session, user_id, user: schemas.User):
    try:
        user_details = get_user(db, user_id)
        if user_details is None:
            logger.warning('User not Updated, User ID not Found')
            raise HTTPException(status_code=404, detail="id Not Found")
        user_details.first_name = user.first_name
        user_details.last_name = user.last_name
        user_details.gender = user.gender
        db.commit()
        db.refresh(user_details)
        logger.info('User Updated: ID {}, first_name:{}, last_name:{}, gender:{}'.format(user_id, user.first_name,
                                                                                            user.last_name,
                                                                                            user.gender))
        return user_details
    except Exception as e:
        logger.exception('Got exception -->> '.format(e))


def delete_user(db: Session, user_id):
    user_details = get_user(db, user_id)
    if user_details is None:
        logger.warning('User not deleted, User ID not Found')
        raise HTTPException(status_code=404, detail="id Not Found")
    try:
        db.delete(user_details)
        db.commit()
        logger.info('User deleted: Id:{}'.format(user_id))
        return {"user deleted": True}
    except Exception as e:
        logger.exception('Got exception -->> '.format(e))
