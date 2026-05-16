from fastapi import APIRouter


router = APIRouter()

@router.post('/')
async def calculate(num1: int, num2: int):
    return {'result': num1 + num2}
