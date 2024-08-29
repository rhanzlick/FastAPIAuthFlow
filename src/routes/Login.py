import sys, datetime
from typing import Annotated, List, Union, Dict

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import HTMLResponse


from ..models.Authenticator import Authenticator
from ..models.Database import Database, get_db
from ..models.User import User

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

route_name = 'login'

Router = APIRouter(
    prefix=f'/{route_name}',
    tags=[route_name],
    #dependencies=Depends(),
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Page Not Found'},
    },
)

Router.mount('/src/static', StaticFiles(directory='src/static'), name="static")

@Router.post('/')
async def UserSignup(user:User, db:Database = Depends(get_db)):
    if user.username in db.Users:
        raise HTTPException(400, 'Username already exists')
    
    hashed = db.HashPass(user.password)
    db.Users[user.username] = {
        'email':user.email,
        'username':user.username,
        'password': hashed
    }
    return {'message': 'user created successfully'}

