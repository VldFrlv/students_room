from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from .database import async_session, get_session
from .models import users
from .schemas import User

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@auth_router.get('/users')
async def get_users(sesion: AsyncSession = Depends(get_session)) -> List[User]:
    query = select(users)
    result = await sesion.execute(query)
    return result.all()


@auth_router.get('/user/{id}/')
async def get_user(id: int, session: AsyncSession = Depends(get_session)) -> List[User]:
    query = select(users).filter(users.id == id).first()

    if query == None:
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    result = await session.execute(query)
    return result






