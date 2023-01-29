from fastapi import FastAPI
from auth.router import auth_router

app = FastAPI(title='Johan')
app.include_router(auth_router)


