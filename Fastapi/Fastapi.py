from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()
db=[]
class Person(BaseModel):
    name:str


@app.get("/")
def fn1():return db

# post : http://0.0.0.0:5000/person/deepak?num=1&b=true
# body = {"name":"deepak"}
@app.post("/person/{name}")
def fn2(num:int,person:Person,b:bool):
    db.append(person)
    return db #dict

