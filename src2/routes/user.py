import uuid

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

class User(BaseModel):

    username:str
    email:str
    password:str
    ID: uuid.UUID = None

# from src2.models import auth
# from app.src2.models import auth
from models import auth

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

route_name = 'user'

router = APIRouter(
    prefix=f'/{route_name}',
    tags=[route_name],
    #dependencies=Depends(),
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Page Not Found'},
    },
)

#In[] methods

# async def validate_user(token:str = Depends(oauth2_scheme)):

#     raw_token = decode_token(token)
#     # user_creds = full_db['users'].get(raw_token)
#     user_creds = full_db['users'].get(raw_token.username)
#     if user_creds:
#         return User(**user_creds)
#     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or missing token")

#In[] Routes

@router.get("/me")
async def get_user(current_user: User = Depends(auth.get_current_user)):
    return current_user


@router.post("/create")
async def create_user(current_user: User):

    pass
    # user_record = full_db['users'].get(new_user.username)
    # if user_record:
    #     # raise HTTPException(status_code=400, detail="Username Exists")
    #     return JSONResponse(content={'message':'username already exists'} ,status_code=status.HTTP_400_BAD_REQUEST)

    # new_user.password = hash_pass(new_user.password)

    # if insert_user(new_user):
    #     return JSONResponse(content={'message':'new user created - thanks!'}, status_code=status.HTTP_201_CREATED)



#In[]

if __name__ == '__main__':
    quit(0)