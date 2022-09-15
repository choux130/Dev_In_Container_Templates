# %%
import os
import sys
from fastapi import FastAPI

sys.path.append(os.path.realpath('../'))
from src.myfuns import AddTen

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/addten/")
def add_ten(x: int):
    return AddTen(x)