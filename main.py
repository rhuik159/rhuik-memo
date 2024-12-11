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
    for m in memos:
        if m.id==id:
            m.content=memo.content
            return '성공했습니다'
    return '그런 메모는 없습니다'

app.mount("/",StaticFiles(directory="static",html=True),name="static")
