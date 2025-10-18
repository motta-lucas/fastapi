from pydantic import BaseModel, ConfigDict
from typing import List

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

class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = ConfigDict(
        json_schema_extra = {
            "examples": {
                "todos":[
                    {
                        "item":"Example schema 1!"
                    },
                    {
                        "item":"Example schema 2!"
                    }
                ]
            }
            
        }
    )
    