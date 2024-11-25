from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from fastapi import APIRouter, Request, Depends, HTTPException

token_path = 'token'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = token_path)

route_name = 'auth'

router = APIRouter(
    prefix=f'/{route_name}',
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
    pass

@router.post(f'/{token_path}')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    #check if username is in db
    #check if entered pass matches hashed pass
    #return token
    token = ''
    return {'token_type':'bearer', 'access_token':token}

    # user_record = full_db['users'].get(form_data.username)
    # if not user_record:
    #     raise HTTPException(status_code=400, detail="Incorrect username or password")
    # user = User(**user_record)
    # # if hash_pass(form_data.password) == user.password:
    # if validate_pass(form_data.password, user.password):
    #     # token = get_token(user)
    #     token = get_token(vars(user))
    #     return {'access_token':token, 'token_type':'bearer'}