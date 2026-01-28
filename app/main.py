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

# E.g. https://localhost:8000/item?id=1
@app.get("/item")
async def get_item(id=None):
    list_to_debug = [item["item_id"] for item in items]
    print(list_to_debug)
    return_json = {"name": ""}
    for item in items:
        if item["item_id"] == int(id):
            return_json = {"name": item["name"]}
            break
        else:
            return_json = {"name": "not found"}
    return return_json



