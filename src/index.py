import uuid, secrets, asyncio
from typing import Annotated, List, Union, Dict

from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

import json
from passlib.context import CryptContext

from pydantic import BaseModel
# from starlette.staticfiles import StaticFiles
# from starlette.responses import RedirectResponse
# from starlette.templating import Jinja2Templates


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# templates = Jinja2Templates(directory='src/templates')

from models.Token import Token
from models.User import User
# from models.User import User
# from models.Authenticator import Authenticator

#from routes.Pages import Router as PageRouter
from routes.User import Router as UserRoutuer
#from routes.SignUp import Router as SignUpRouter

#In[] app Initialization

app = FastAPI()

token_path = 'auth'

oauth_scheme = OAuth2PasswordBearer(tokenUrl = token_path)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=[''],
    allow_methods=['*'],
    allow_headers=['*'])

#In[] User Auth Utils

pwd_context = CryptContext(schemes='bcrypt')

def hash_pass(raw_pass:str):
    
    # return f'hashed_{raw_pass}'
    return pwd_context.hash(raw_pass)

def validate_pass(raw_pass, hashed_pass) -> bool:

    return pwd_context.verify(raw_pass, hashed_pass)

def get_token(user:Union[User, dict]) -> str:

    # return f'encoded_{user.username}'
    return Token.Encode(user)
    

# def decode_token(token:str) -> str:
def decode_token(token:str) -> Token:

    # user = User(username = f'{token}_decoded',)
    # return token.strip('encoded_')
    return Token.Decode(token)

# async def validate_user(token: Annotated[str, Depends(oauth_scheme)]):
# async def validate_user(token:str = Depends(oauth_scheme)) -> User:
async def validate_user(token:str = Depends(oauth_scheme)) -> User:

    raw_token = decode_token(token)
    # user_creds = full_db['users'].get(raw_token)
    user_creds = full_db['users'].get(raw_token.username)
    if user_creds:
        return User(**user_creds)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or missing token")

def insert_user(user:User) -> bool:

    try:
        full_db['users'][user.username] = vars(user)
        full_db['items'][user.username] = []
        return True
    except Exception as ex:
        #log error
        print(ex, flush=True)
        return False


full_db:Dict[str, Dict[str,Dict[str,Union[str, List[str]]]]] = {
    'users':{
        'u':{'username':'u', 'password':pwd_context.hash('p'), 'email':'u@u.com'},
    },
    'items':{
        'u':['item1','item2'],
    }
}



#In[] Items

class Item(BaseModel):
    
    name:str = None
    u_id:str = None

@app.get('/items')
async def get_items(req:Request, user: Annotated[User, Depends(validate_user)]) -> bool:
    
    user_items = full_db['items'].get(user.username)
    if user_items:
        user_items = full_db['items'][user.username]
        # data = [Item(name=i,u_id=user.username) for i in user_items]
        data = [{'name':i,'u_id':user.username} for i in user_items]
        return JSONResponse(content={'items':data}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={'message':'invalid or missing token'}, status_code=status.HTTP_403_FORBIDDEN)

#In[] Routes

@app.get('/')
async def root():
    
    return {'routes':', '.join([str(r.path) for r in app.routes])}

@app.get('/users/')
# async def get_user(token: Annotated[str, Depends(oauth_scheme)]):
async def db_dump():

    # return [u for u in full_db['users'].items()]
    return [u for u in full_db.items()]

@app.get('/user/')
# async def get_user(token: Annotated[str, Depends(oauth_scheme)]):
async def get_user(user:User = Depends(validate_user)):

    return user



@app.post('/user/create')
# async def create_user(request:Request, form_data: OAuth2PasswordRequestForm = Depends()):
async def create_user(new_user:User):

    user_record = full_db['users'].get(new_user.username)
    if user_record:
        # raise HTTPException(status_code=400, detail="Username Exists")
        return JSONResponse(content={'message':'username already exists'} ,status_code=status.HTTP_400_BAD_REQUEST)

    new_user.password = hash_pass(new_user.password)

    if insert_user(new_user):
        return JSONResponse(content={'message':'new user created - thanks!'}, status_code=status.HTTP_201_CREATED)
    

@app.post(f'/{token_path}')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user_record = full_db['users'].get(form_data.username)
    if not user_record:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User(**user_record)
    # if hash_pass(form_data.password) == user.password:
    if validate_pass(form_data.password, user.password):
        # token = get_token(user)
        token = get_token(vars(user))
        return {'access_token':token, 'token_type':'bearer'}



# app.include_router(UserRoutuer)
# app.include_router(PageRouter)
#app.include_router(SignUpRouter)


if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("src.index:app", host="0.0.0.0", port=8_000, reload=True)
    uvicorn.run("index:app", host="0.0.0.0", port=8_000, reload=True)

