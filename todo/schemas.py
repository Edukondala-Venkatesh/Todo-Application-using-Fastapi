from pydantic import BaseModel
from typing import List, Optional, TypeVar, Generic
# from pydantic.generics import GenericModel




class Blog(BaseModel):
    title        : str
    description  : str


class TodoUpdate(BaseModel):
    title: str
    description: str
    completed: bool = False
    
class User(BaseModel):
    id      : int
    name    : str
    email   : str
    password: str

class ShowUser(BaseModel):
    name    : str
    email   : str
    class Config():
        from_attributes = True



class ShowBlog(BaseModel):
    title        : str
    description  : str
    completed    : bool
    user_id      : int
    # creator      : Optional[ShowUser]

    class Config():
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

T = TypeVar('T')

class PageResponse(BaseModel, Generic[T]):
    """ The response for a pagination query. """

    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: List[T]

class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None