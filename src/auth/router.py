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
from .schemas import User, UserPatch, UserLogin, Token

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


@auth_router.post('/refresh/')
async def refresh_token(request: Request, refresh: Token):
    refresh_token = refresh

    return auth.get_new_refresh_or_401(refresh_token.refresh)


@auth_router.get('/get_all_users')
async def get_all_users(request: Request, session: AsyncSession = Depends(get_session)) -> List[User]:
    try:
        access_token = request.headers.get('authorization')
        if auth.decode_access_token(access_token):
            users_query = select(users)
            all_users = await session.execute(users_query)
            return all_users.all()

    except Exception:
        raise HTTPException(status_code=401, detail='authorization data not provided')
