from typing import Optional, Field

from pydantic import BaseModel

from fastapi import FastAPI
from fastapi import Body, Query, Path
from fastapi.responses import JSONResponse

app = FastAPI()

# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Field(default="Black", min_lenght=2 ,max_lenght=6)
    is_married: Optional[bool] = None

    class Config:
        schema_extra = {
            'id': 1,
            'title': 'Missing title',
        }

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
    return JSONResponse(content={name: age}) 

# Validaciones path parameters
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(..., gt=0)
):
    return {person_id: 'It existsss'}
