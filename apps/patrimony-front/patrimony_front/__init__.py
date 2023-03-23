import uvicorn

def start():
    uvicorn.run('patrimony_front.main:app', reload=True)