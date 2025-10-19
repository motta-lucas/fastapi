from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from fastapi import Form

class PacktBook(BaseModel):
    id: str
    Name: str
    Publishers: str
    Isbn: str

class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
    ):
        return cls(item=item)

    model_config = ConfigDict(
        json_schema_extra = {
            "examples": [{
                "id": 1,    
                "item": "Example schema!"
            }
            ]
        }
    )
    

    
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
    