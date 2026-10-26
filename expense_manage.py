from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel,Field
from typing import Literal

app=FastAPI()

category=["Groceries","Rent","Food","Transport","Shopping","Entertainment","Healthcare","Others"]
class Transaction:
    amount:float
    transaction_type:str
    categories:str

@app.get('/')
def getting_details(amount:float,
    transaction_type:str,
    categories:str):
    if categories not in category:
        raise HTTPException(status_code=400,details="Invalid category details")
    return {"amount":amount,"categories":categories,"transaction_type":transaction_type}

@app.post('/')
def posting(amount:float,
    transaction_type:str,
    categories:str):
     return {"amount":amount,"categories":categories,"transaction_type":transaction_type}


