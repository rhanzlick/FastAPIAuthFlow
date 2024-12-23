import os, sys, logging

from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

# from routes.user import *
# from routes.pages import *
from models import auth
from routes import user
from routes import item

#In[]

# token_path = 'auth'
# oauth_scheme = OAuth2PasswordBearer(tokenUrl = token_path)
# pwd_context = CryptContext(schemes='bcrypt')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=[''],
    allow_methods=['*'],
    allow_headers=['*'])

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(item.router)

# app.include_router()

#In[]
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        app = 'index:app',
        host = '0.0.0.0',
        port = 8_000,
        reload = True
    )