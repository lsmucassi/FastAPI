from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {
            "data": {
                f"{limit} published blogs to retrive"
            }
        }
    return {
        "data": {
            f"{limit} blogs to retrive"
        }
    }


@app.get("/blog/unpublished")
def unpublished(id: int):
    return {
        "data": "All Unpublished Blogs"
    }


@app.get("/blog/{id}")
def show(id: int):
    return {
        "data": id
    }


@app.get("/blog/{id}/comments")
def comments(id: int, limit=10):
    return {
        "data": {
            "comments": {
                "comment one", "cmment two"
            }
        }
    }


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(request: Blog):
    return {"data": {f"blog is created with title {request.title}"}}
