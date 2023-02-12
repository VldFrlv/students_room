import datetime
from typing import List, Callable

from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.responses import Response, RedirectResponse

from database import get_session

from .models import users
from .schemas import User, UserPatch, UserLogin

from jose import jwt

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

secret = 'johan'


@auth_router.post('/login')
async def user_login(data: UserLogin, session: AsyncSession = Depends(get_session)):
    try:
        user = select(users).where(users.c.email == data.email)
        get_user = await session.execute(user)
        if data.password == get_user.fetchone()[3]:
            access = jwt.encode({'email': data.email, 'password': data.password,
                                 "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}, secret,
                                algorithm='HS256')
            refresh = jwt.encode({'email': data.email, 'password': data.password,
                                 "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, secret,
                                algorithm='HS256')
            return {
                'access': access,
                'refresh': refresh
            }
        else:
            return {"message": "Email or password not valid"}

    except Exception:
        return {"message": "Email or password not valid"}


# def authorization(handler: Callable):
#
#     def inner(*args, **kwagrs):



@auth_router.post('/authorization')
async def authorization(request: Request, session: AsyncSession = Depends(get_session)):
    access = request




@auth_router.post('/auth')
async def get_authorization(request: Request, session: AsyncSession = Depends(get_session)):
    token = request.get('headers')[6][1]
    try:
        decoded_token = jwt.decode(token, secret, algorithms=['HS256'])
        user = select(users).where(users.c.email == decoded_token['email'])
        get_user = await session.execute(user)
        id = get_user.first()[0]
        return {'id': id}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
