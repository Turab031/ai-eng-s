from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
async def root():
    return {"message":"Hello World,kaisa hai"}


@app.get("/")
async def root():
    return {"message":"fastap"}



@app.get("/blog/comments")
async def read_blog():
    return {"message":"no comments yet"}

@app.get("/blog/{blog_id}")
async def get_blog(blog_id:int,q:str=None,name:str=''):
    print(q,name)
    return {"blog_id":blog_id}

# specific baad me ata h
# @app.get("/blog/comments")
# async def read_blog():
#     return {"message":"no comments yet"}