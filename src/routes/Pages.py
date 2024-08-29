import sys, datetime
from typing import Annotated, List, Union, Dict

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
#from fastapi.responses import HTMLResponse


# from ..models.Authenticator import Authenticator
# from ..models.Database import Database, get_db
# from ..models.User import User

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# templates = Jinja2Templates(directory='src/templates')
templates = Jinja2Templates(directory='src/templates')

route_name = 'pages'

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

@Router.get('/signup')
async def SignUpPage(req:Request):
    context = {
        'request':req,
    }
    return templates.TemplateResponse('signup.html', context)

@Router.get('/home')
async def SignUpPage(req:Request):
    context = {
        'request':req,
    }
    return templates.TemplateResponse('home.html', context)

