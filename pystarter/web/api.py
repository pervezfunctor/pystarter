from enum import Enum
from typing import Any
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


# Hello World


@app.get("/")
async def root():
    return {"message": "Hello World FastAPI"}


# Path Parameters


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Query parameters


@app.get("/uitems/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
) -> dict[Any, Any]:
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


# Request body


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# Validation of parameters


@app.get("/sitems/")
async def read_items(q: str | None = Query(None, title="Query string", min_length=3)):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/nitems/{item_id}")
async def read_nitems(
    item_id: int = Path(..., title="The ID of the item to get", gt=0),
    q: str | None = Query(None, alias="item-query"),
):
    results: dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
