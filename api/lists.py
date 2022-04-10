from fastapi import APIRouter
from fastapi import Depends
from api import dependencies
from services import lists
from models.list import ListInput, List
from pymongo.database import Database

router = APIRouter(prefix="/lists", tags=["lists"])


@router.get("")
async def get_all_lists(db: Database = Depends(dependencies.get_db)):
    return lists.read_all_lists(db)

@router.post("")
async def create_list(l: ListInput, db: Database = Depends(dependencies.get_db)):
    return lists.create_list(db, l)

@router.put("/{list_id}")
async def update_list(list_id: str, data: ListInput, db: Database = Depends(dependencies.get_db)):
    return lists.update_list(db, list_id, data)

@router.delete("/{list_id}")
async def delete_list(list_id: str, db: Database = Depends(dependencies.get_db)):
    return lists.delete_list(db, list_id)

@router.get("/{list_id}")
async def get_list(list_id: str,  db: Database = Depends(dependencies.get_db)):
    return lists.read_list(db, list_id)
