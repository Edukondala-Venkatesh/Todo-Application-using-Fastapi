from fastapi import APIRouter,Depends,Response,HTTPException,status
from sqlalchemy.orm import Session
from typing import List
from todo import schemas, database, models
from todo.Repository import userRepository

router = APIRouter(
    prefix ='/user',
    tags=['User'])

get_db = database.get_db


@router.post('/')
def user(request : schemas.User,db :Session = Depends(get_db)):
    return userRepository.create_user(request,db)


@router.get('/{id}',response_model=schemas.ShowUser)
def show(id:int, db: Session = Depends(get_db)):
    return userRepository.get_user(id,db)

@router.get('/')
def All(db : Session = Depends(database.get_db)):
    return userRepository.get_all(db)