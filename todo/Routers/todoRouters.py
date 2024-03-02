from fastapi import APIRouter,Depends,Response,HTTPException,status
from sqlalchemy.orm import Session
from typing import Annotated, List
from todo import schemas, database, models, oauth2
from todo.Repository import todoRepository
from todo.schemas import Blog


router = APIRouter(
    prefix = "/todo",
    tags=["Todo"]
)

get_db = database.get_db


@router.get('/')
def all(db : Session = Depends(database.get_db), current_user: dict = Depends(oauth2.get_current_user)):
    return todoRepository.get_all(db)

@router.post('/', status_code = 201)
def create(request : Blog,db : Session = Depends(get_db), current_user: dict = Depends(oauth2.get_current_user)):
    todo_model = models.Blog(**request.dict(), user_id=current_user.get('id'))
    db.add(todo_model)
    db.commit()
    return f"New Todo Activate is Created"

@router.delete('/', status_code=status.HTTP_202_ACCEPTED)
def destroy(id:int ,db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todoRepository.Destroy(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request : schemas.TodoUpdate, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todoRepository.update(id,request,db)

@router.get('/{id}', status_code=status.HTTP_202_ACCEPTED,response_model=schemas.ShowBlog)
def show(id :int,db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todoRepository.show(id,db)



