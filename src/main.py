from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from auth.router import auth_router
from app_admin.router import admin_router

from fastapi.templating import Jinja2Templates

app = FastAPI(title='Johan')
app.include_router(auth_router)
app.include_router(admin_router)

app.mount('/static', StaticFiles(directory='static'))

templates = Jinja2Templates(directory='templates')


@app.get('/login_form', response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse('login_form.html', {'request': request})


@app.get('/user_page', response_class=HTMLResponse)
async def get_user_page(request: Request):
    return templates.TemplateResponse('user_page.html', {'request': request})