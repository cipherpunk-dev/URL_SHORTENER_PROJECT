import validators
from fastapi import FastAPI as FAPI,HTTPException
from . import schemas #dot means from this directory

app=FAPI()

def raise_bad_request(message): #just for my convenience , helper function kinda
    raise HTTPException(status_code=400,detail=message)

@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="Provided URL is not valid")
    return f"To do Create Database entry for {url.target_url}"
