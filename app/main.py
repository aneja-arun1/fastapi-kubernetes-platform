from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "In Root"}
@app.get("/items/{item_id}")
async def get_items_by_item(item_id: int):
    return {"item_id": item_id}

