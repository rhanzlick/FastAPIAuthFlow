import sys, datetime, json
from typing import Annotated, List, Union, Dict
from pydantic import BaseModel

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi.responses import HTMLResponse

#from models.Authenticator import Authenticator
from models.Database import Database, get_db, db
#from ..models.Database import Database, get_db

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

class User(BaseModel):
    email:str
    username:str
    password:str

#db = Database()

# templates = Jinja2Templates(directory='src/templates')
# templates = Jinja2Templates(directory='templates')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

route_name = 'user'

Router = APIRouter(
    prefix=f'/{route_name}',
    tags=[route_name],
    #dependencies=Depends(),
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Page Not Found'},
    },
)

# Router.mount('/src/static', StaticFiles(directory='src/static'), name="static")
# Router.mount('/static', StaticFiles(directory='static'), name="static")

@Router.get('/')
# async def SignUpPage(req:Request):
async def GetUserTest():
    return {'users':'page'}

@Router.get('/{username}')
# async def SignUpPage(req:Request):
# async def GetUser(username:str, db:Database = Depends(get_db)):
async def GetUser(username:str):
    if username == '*':
        return db.Users
    else:
        return db.Users[username]

@Router.post('/create')
# async def CreateUser(user:User, db:Database = Depends(get_db)):
async def CreateUser(user:User):

    print(user)

    if user.username in db.Users:
        raise HTTPException(400, 'Username already exists')

    user.password = db.HashPass(user.password)
    db.Users[user.username] = vars(user)

    return {'message': 'user created successfully'}

@Router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = db.Users[form_data.username]
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = User(**user_dict)

    hashed_password = db.HashPass(form_data.password)
    if hashed_password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@Router.post('/login')
# async def LoginUser(user:User, db:Database = Depends(get_db)) -> User:
async def LoginUser(token: Annotated[str, Depends(oauth2_scheme)]) -> User:

    return {'token': token}
    # user.password = db.HashPass(user.password)
    # db.Users[user.username] = vars(user)

    return 

