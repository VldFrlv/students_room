from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from .models import users
from .schemas import User

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@auth_router.get('/users')
async def get_users(session: AsyncSession = Depends(get_session)) -> List[User]:
    query = select(users)
    result = await session.execute(query)
    return result.all()


@auth_router.get('/add__users')
async def get_users(user_data: User, session: AsyncSession = Depends(get_session)):
    query = insert(users).values(**user_data.dict())
    await session.execute(query)
    await session.commit()
    return User(user_data)


