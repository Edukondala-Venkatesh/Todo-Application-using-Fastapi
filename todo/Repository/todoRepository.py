from fastapi import HTTPException,status,Depends
from sqlalchemy.orm import Session 
from todo import models,schemas


# Execute all in database
def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

# Create data in database
def create(request: schemas.Blog, user_id, db:Session):
    new_blog= models.Blog(**request.dict())
    new_blog.user_id = user_id
    db.add(new_blog)
    db.commit()
    return f"New Todo Activate is Created"

# Delete data in database
def Destroy(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")    
    blog.delete(synchronize_session = False)
    db.commit()
    return f'id {id} record is Deleted'

# Update data in database
def update(id, request : schemas.TodoUpdate, db : Session ):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")

    blog.update(dict(request))
    db.commit()
    return f'id {id} record is updated'

# Execute data based on id in database
def show(id,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")
    print(blog)
    return blog

