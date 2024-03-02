from fastapi import APIRouter, Query
from sqlalchemy.orm import Session
from todo import schemas, database, models, oauth2
from todo.Repository import FilterRepository


router = APIRouter(
    prefix = "/filter",
    tags=["Filter"]
)

get_db = database.get_db

@router.get("", response_model=schemas.ResponseSchema, response_model_exclude_none=True)
async def get_all_person(
        page: int = 1,
        limit: int = 10,
        columns: str = Query(None, alias="columns"),
        sort: str = Query(None, alias="sort"),
        filter: str = Query(None, alias="filter"),
):
    result = await FilterRepository.get_all(page, limit, columns, sort, filter)
    return schemas.ResponseSchema(detail="Successfully fetch person data by id !", result=result)