MOCK_ROOMS = [
    {
        "id": 1,
        "name": "Conference Room A",
        "description": "Meeting room for small teams",
        "capacity": 8,
        "location": "Floor 2 / Room 205",
        "isActive": True,
        "imageUrl": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=600&fit=crop",
    },
    {
        "id": 2,
        "name": "Conference Room B",
        "description": "Large room for presentations",
        "capacity": 20,
        "location": "Floor 1 / Room 101",
        "isActive": False,
        "imageUrl": "https://images.unsplash.com/photo-1431540015161-0bf868a2d407?w=800&h=600&fit=crop",
    },
    {
        "id": 3,
        "name": "Focus Room",
        "description": "Quiet space for deep work or 1:1 calls",
        "capacity": 2,
        "location": "Floor 3 / Room 312",
        "isActive": True,
        "imageUrl": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=800&h=600&fit=crop",
    },
    {
        "id": 4,
        "name": "Training Hall",
        "description": "Spacious hall for workshops and training sessions",
        "capacity": 40,
        "location": "Floor 1 / Room 110",
        "isActive": True,
        "imageUrl": "https://images.unsplash.com/photo-1517502884422-41eaead166d4?w=800&h=600&fit=crop",
    },
    {
        "id": 5,
        "name": "Board Room",
        "description": "Executive meeting room with video conference setup",
        "capacity": 12,
        "location": "Floor 4 / Room 401",
        "isActive": True,
        "imageUrl": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=800&h=600&fit=crop",
    },
    {
        "id": 6,
        "name": "Brainstorm Studio",
        "description": "Creative room with whiteboards and sticky walls",
        "capacity": 10,
        "location": "Floor 2 / Room 218",
        "isActive": False,
        "imageUrl": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=800&h=600&fit=crop",
    },
]


def get_mock_list():
    return [room.copy() for room in MOCK_ROOMS]

def add_to_mock_list(room: dict) -> dict:
    new_room = room.copy()
    if "id" not in new_room:
        new_room["id"] = max((r["id"] for r in MOCK_ROOMS), default=0) + 1
    MOCK_ROOMS.append(new_room)
    return new_room.copy()

def get_item_by_id(room_id: int) -> dict | None:
    for room in MOCK_ROOMS:
        if room["id"] == room_id:
            return room.copy()
    return None

def delete_item_by_id(room_id: int) -> bool:
    for index, room in enumerate(MOCK_ROOMS):
        if room["id"] == room_id:
            MOCK_ROOMS.pop(index)
            return True
    return False