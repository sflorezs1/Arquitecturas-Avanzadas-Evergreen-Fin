import uvicorn

def start():
    uvicorn.run('patrimony_back.main:app')