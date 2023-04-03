from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

app.title  = 'App with FastAPI'

app.version = '0.0.1'

@app.get('/', tags=['home'])
def home():
    return {'Hello':'World'}

## Creating of Request and Response body
@app.post('/person/new')
def create_client(person: Person = Body):
    return person

