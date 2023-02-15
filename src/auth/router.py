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

from .service import Auth

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

auth = Auth()


@auth_router.post('/login')
async def user_login(data: UserLogin, session: AsyncSession = Depends(get_session)):
    try:
        user = select(users).where(users.c.email == data.email)
        get_user = await session.execute(user)
        if data.password == get_user.fetchone()[3]:
            access_token = auth.encode_access_token(data.email)
            refresh_token = auth.encode_refresh_token(data.email)
            return {'access_token': access_token, 'refresh_token': refresh_token}
        else:
            raise HTTPException(status_code=401, detail='Email or password not valid')
    except Exception:
        raise HTTPException(status_code=401, detail='Email or password not valid')


@auth_router.get('/refresh')
async def refresh_token(request: Request):
    refresh_token = request.cookies.get('refresh')
    return auth.get_new_refresh_or_401(refresh_token)


@auth_router.get('/authorization')
async def authorization(request: Request):
    print(request.cookies)
    # access_token = request.cookies.get('access_token')
    # print(access_token)
    # return auth.decode_access_token(access_token)
    return {'ok': 1}




