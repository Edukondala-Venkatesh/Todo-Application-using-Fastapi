from fastapi import HTTPException,status,Depends
from sqlalchemy.orm import Session 
from todo import models,schemas
from todo.hashing import Hash
from fastapi_babel import _


# Create data in User
def create_user(request: schemas.User,db:Session):
    new_blog= models.User(name = request.name,email = request.email,password=Hash.bcrypt(request.password))
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Execute all in database
def get_all(db: Session):
    blogs = db.query(models.User).all()
    return blogs

# Execute data based on id in database
def get_user(id:int,db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        error_message= _("Blog with the id {id} is not available").format(id=id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=error_message)
    return user