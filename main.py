from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Name(BaseModel):
    name: str

class Transcription(BaseModel):
    transcription: str

recognized_names = []
transcriptions = []

@app.post("/names/")
def add_name(name: Name):
    recognized_names.append(name.name)
    return {"message": "Name added successfully", "current_names": recognized_names}

@app.get("/names/")
def get_names():
    return {"recognized_names": recognized_names}

@app.post("/transcriptions/")
def add_transcription(transcription: Transcription):
    transcriptions.append(transcription.transcription)
    return {"message": "Transcription added successfully", "current_transcriptions": transcriptions}

@app.get("/transcriptions/")
def get_transcriptions():
    return {"transcriptions": transcriptions}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Name API!"}
