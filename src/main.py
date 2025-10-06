from fastapi import FastAPI
from pydantic import BaseModel
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import all_process

import json


app = FastAPI()

class FileRequest(BaseModel):
    file_path: str
class ProcessResponse(BaseModel):
    message: str
    output_file: str
class ParsedData(BaseModel):
    data: dict

@app.get("/")
def read_root():
    return {"message": "Welcome to the Resume Parser API"}      


@app.post("/process_file", response_model=ProcessResponse)
def process_file(request: FileRequest):
    try:
        output_file=all_process(request.file_path)

        return ProcessResponse(message="File processed successfully.", output_file=output_file)
    except Exception as e:
        return ProcessResponse(message=f"Error processing file: {str(e)}", output_file="")
    
    
@app.post("/get_parsed_data", response_model=ParsedData)
def get_parsed_data(request: ProcessResponse):
    try:
        with open(request.output_file, 'r') as f:
            data = json.load(f)
        return ParsedData(data=data)
    except Exception as e:
        return ParsedData(data={"error": str(e)})