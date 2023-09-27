# This is the sample from https://fastapi.tiangolo.com/

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Category(BaseModel):
    category_id: int
    name: str
    description: str


class Item(BaseModel):
    item_id: int
    name: str
    price: float
    is_offer: Union[bool, None] = None
    category: Category


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    cat = Category(name="Toys", category_id=1234, description="Toys for kids")
    item = Item(item_id=2, name="Toy Car", price=123.45, category=cat)
    return {item: item, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# skip and limit (if supplied) would come from the querystring and will be converted to int
# would match ex:
#   http://127.0.0.1:8000/items/?skip=666
#   http://127.0.0.1:8000/items
# will cause error:
#   http://127.0.0.1:8000/items/?skip=foo  (because foo is not an int)
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"fake_results": {"your_params": {"skip": skip, "limit": limit}}}
