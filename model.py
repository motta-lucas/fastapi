from pydantic import BaseModel

class PacktBook(BaseModel):
    id: str
    Name: str
    Publishers: str
    Isbn: str

class Todo(BaseModel):
    id: int
    item: str
