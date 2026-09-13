from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils.fake_db import (
    add_to_mock_list,
    delete_item_by_id,
    get_item_by_id,
    get_mock_list,
)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

PREFIX_API = "/api"


class RoomCreate(BaseModel):
    name: str
    description: str
    capacity: int
    location: str
    isActive: bool
    imageUrl: str | None = None


class RoomOut(BaseModel):
    id: int
    name: str
    description: str
    capacity: int
    location: str
    isActive: bool
    imageUrl: str | None = None


@app.get(f"{PREFIX_API}/rooms", response_model=list[RoomOut])
def get_room_list():
    return get_mock_list()


@app.get(f"{PREFIX_API}/rooms/{{room_id}}", response_model=RoomOut)
def get_room_by_id(room_id: int):
    room = get_item_by_id(room_id)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@app.post(f"{PREFIX_API}/rooms", response_model=RoomOut, status_code=201)
def create_room(room: RoomCreate):
    return add_to_mock_list(room.model_dump())


@app.delete(f"{PREFIX_API}/rooms/{{room_id}}", status_code=204)
def delete_room(room_id: int):
    deleted = delete_item_by_id(room_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Room not found")
