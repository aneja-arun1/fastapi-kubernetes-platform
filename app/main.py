from fastapi import FastAPI
app = FastAPI()
items = [
    {"item_id": 1, "name": "orange"},
    {"item_id": 2, "name": "apple"}, ]

@app.get("/")
async def root():
    return {"message": "In Root"}

@app.get("/items/{item_id}")
async def get_item_by_item_id(item_id: int):
    return_json = {"name": ""}
    for item in items:
        if item["item_id"] == item_id:
            return_json = {"name": item["name"]}
    return return_json


