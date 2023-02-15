from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi.responses import RedirectResponse

from auth.models import users
from auth.router import auth_router
from app_admin.router import admin_router

from fastapi.templating import Jinja2Templates

from database import get_session

app = FastAPI(title='Johan')
app.include_router(auth_router)
app.include_router(admin_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,

    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static', StaticFiles(directory='static'))

templates = Jinja2Templates(directory='templates')


@app.get('/login_form', response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse('login_form.html', {'request': request})


@app.get('/user_page', response_class=HTMLResponse)
async def get_user_page(request: Request, session: AsyncSession = Depends(get_session)):
    # try:
    #     bearer = request._cookies.get('bearer')
    #     decoded_token = jwt.decode(bearer, secret, algorithms=['HS256'])
    #     user_query = select(users).where(users.c.email == decoded_token.get('email'))
    #     user = await session.execute(user_query)
    #     user_data = user.fetchone()
    return templates.TemplateResponse('user_page.html', {'request': request})

    # except Exception:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid authentication credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )


@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("http://127.0.0.1:8000/user_page")
