from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Name(BaseModel):
    name: str

# This will store all the names received
recognized_names = []

@app.post("/names/")
def add_name(name: Name):
    recognized_names.append(name.name)
    return {"message": "Name added successfully", "current_names": recognized_names}

@app.get("/names/")
def get_names():
    return {"recognized_names": recognized_names}
