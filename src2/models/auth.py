from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from fastapi import APIRouter, Request, Depends, HTTPException

import uuid

# token_path = 'token'
token_path = 'login'
route_name = 'auth'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = f'{token_path}')


router = APIRouter(
    # prefix=f'/{route_name}',
    tags=[route_name],
    #dependencies=Depends(),
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Page Not Found'},
    },
)

# auth.py
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Validate token and return user
    uname, password, ID = token.split('|')
    return {
        'username':uname,
        'email':'',
        'password':password,
        'ID': uuid.UUID(ID) if ID else None,
    }

    

@router.post(f'/{token_path}')
# @router.post(f'/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    #check if username is in db
    #check if entered pass matches hashed pass
    #return token
    token = uuid.uuid4()
    return {'token_type':'bearer', 'access_token':f'{form_data.username}|{form_data.password}|{str(token)}'}

    # user_record = full_db['users'].get(form_data.username)
    # if not user_record:
    #     raise HTTPException(status_code=400, detail="Incorrect username or password")
    # user = User(**user_record)
    # # if hash_pass(form_data.password) == user.password:
    # if validate_pass(form_data.password, user.password):
    #     # token = get_token(user)
    #     token = get_token(vars(user))
    #     return {'access_token':token, 'token_type':'bearer'}