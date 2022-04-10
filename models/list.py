from dataclasses import dataclass
from bson import ObjectId
from pydantic import BaseModel


class List(BaseModel):
    id: str
    name: str


class ListInput(BaseModel):
    name: str
        

