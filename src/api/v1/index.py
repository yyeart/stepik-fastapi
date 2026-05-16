from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()

@router.get('/')
async def get_index():
    return FileResponse('src/index.html')