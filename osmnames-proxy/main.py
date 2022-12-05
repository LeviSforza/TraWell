from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{name}")
def get_names(name: str, key: Union[str, None] = None):
    response = requests.get(f"https://search.osmnames.org/PL/q/{name}", params={"key": key})
    return response.json()
