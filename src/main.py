from fastapi import FastAPI

from src.api.v1 import index, calculate


app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World!'}

app.include_router(index.router, prefix="/api/v1/index")
app.include_router(calculate.router, prefix="/api/v1/calculate")
