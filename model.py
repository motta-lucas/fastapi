from pydantic import BaseModel, ConfigDict

class PacktBook(BaseModel):
    id: str
    Name: str
    Publishers: str
    Isbn: str

class Todo(BaseModel):
    model_config = ConfigDict(
        json_schema_extra = {
            "examples": [{
                "id": 1,    
                "item": "Example schema!"
            }
            ]
        }
    )
    
    id: int
    item: str
    
class TodoItem(BaseModel):
    item: str

    model_config = ConfigDict(
        json_schema_extra = {
            "examples": [{   
                "item": "Read the next chapter of the book"
            }
            ]
        }
    )
    