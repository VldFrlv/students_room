from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import HTMLResponse

from database import get_session

from .models import users
from .schemas import User, UserPatch, UserLogin

from jose import jwt


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@auth_router.get('/users')
async def get_users(session: AsyncSession = Depends(get_session)) -> List[User]:
    query = select(users)
    result = await session.execute(query)
    return result.all()


@auth_router.get('/user/{id}')
async def get_user_by_id(id: int, session: AsyncSession = Depends(get_session)) -> User:
    user = select(users).where(users.c.id == id)
    result = await session.execute(user)
    return result.first()


@auth_router.post('/add_user/')
async def get_users(user_data: User, session: AsyncSession = Depends(get_session)):
    new_user = insert(users).values(**user_data.dict())
    await session.execute(new_user)
    await session.commit()
    return {'status': 'success'}


@auth_router.patch('/user_path/{id}')
async def user_path(id: int, user_patch: UserPatch, session: AsyncSession = Depends(get_session)) -> User:
    user = dict(user_patch)
    for key in user.copy():
        if user[key] == None:
            user.pop(key)
    update_user = update(users).where(users.c.id==id).values(**user)
    await session.execute(update_user)
    await session.commit()
    updated_user = select(users).where(users.c.id==id)
    result = await session.execute(updated_user)
    return result.first()


@auth_router.delete('/user/{id}')
async def user_delete(id: int, session: AsyncSession = Depends(get_session)):
    delete_user = delete(users).where(users.c.id==id)
    await session.execute(delete_user)
    await session.commit()
    return {'result': 'success'}


@auth_router.delete('/del/{id}')
async def delete_user(id: int, session: AsyncSession = Depends(get_session)):
    user = delete(users).where(users.c.id == id)
    await session.execute(user)
    return {'result': 'success'}



secret = 'johan'

@auth_router.post('/login')
async def user_login(form_data: UserLogin, session: AsyncSession = Depends(get_session)):
    print(form_data)
    try:
        user = select(users).where(users.c.email == form_data.email)
        get_user = await session.execute(user)
        if form_data.password == get_user.fetchone()[3]:
            token = jwt.encode({'email': form_data.email, 'password': form_data.password}, secret, algorithm='HS256')
            return {"bearer": token}
        else:
            return {"message": "Email or password not valid"}
    except Exception:
        return {"message": "Email or password not valid"}



@auth_router.post('/auth')
async def get_authorization(token: str, session: AsyncSession = Depends(get_session)) -> User:
    try:
        decoded_token = jwt.decode(token, secret, algorithms=['HS256'])
        user = select(users).where(users.c.email == decoded_token['email'])
        get_user = await session.execute(user)
        return get_user.first()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )





