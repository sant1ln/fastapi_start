from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI
from fastapi import Body, Query, Path

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
def create_client(person: Person = Body(...)):
    return person

# Validations query params
@app.get('/person/detail')
def show_client(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: str = Query(...)  
):
    return {name: age}

# Validaciones path parameters
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(..., gt=0)
):
    return {person_id: 'It existsss'}
