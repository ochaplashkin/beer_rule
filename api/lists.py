from fastapi import APIRouter

router = APIRouter(prefix="/lists", tags=["lists"])


@router.get("")
async def get_all_lists():
    return [1,2,3]

@router.post("/{_id}")
async def create_list(_id: str):
    return f"list[{_id}] created"

@router.put("/{_id}")
async def update_list(_id: str):
    return f"list[{_id}] updated"

@router.delete("/{_id}")
async def delete_list(_id: str):
    return f"list[{_id}] deleted"

@router.get("/{_id}")
async def get_list(_id: str):
    return f"list[{_id}]"
