from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Memo(BaseModel):
    id:str
    content:str
    

memos = []

app=FastAPI()

@app.post("/memos")
async def create_memo(memo:Memo):
    memos.append(memo)
    return '메모추가에 성공했습니다.'

@app.get("/memos")
async def read_memo():
    return memos

@app.put("/memo/{id}")
def put_memo(memo:Memo):
    for memo in memos:
        if memo.id==id:
            memo.content=

app.mount("/",StaticFiles(directory="static",html=True),name="static")
