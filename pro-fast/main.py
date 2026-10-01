from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Custom(BaseModel):
    name:str
    age:int



@app.get("/ping")
async def root():
    return {"message":"Hello World,kaisa hai"}


@app.get("/")
async def root():
    return {"message":"fastap"}



@app.get("/blog/comments")
async def read_blog():
    return {"message":"no comments yet"}

@app.post("/blog/{blog_id}")
async def get_blog(blog_id:int,request_body:Custom,  q:str=None,name:str=''):
    print(request_body)
    print(q,name)
    return {"blog_id":blog_id}

# specific baad me ata h
# @app.get("/blog/comments")
# async def read_blog():
#     return {"message":"no comments yet"}