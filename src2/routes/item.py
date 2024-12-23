import uuid
from typing import List, Union
from pydantic import BaseModel
import random

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

from models import auth
from routes.user import User
# from app.src2.models import auth
# from app.src2.routes.user import User

class Item(BaseModel):
    ID: uuid.UUID = None
    description:str = ''
    user_id: uuid.UUID = None

    @staticmethod
    def GetItems(user_id: uuid.UUID) -> List['Item']:

        items = []
        for idx in range(random.randint(0, 10)):
            items.append(
                Item(
                    ID = uuid.uuid4(),
                    description = f'this is item: {idx}',
                    user_id = user_id
                )
            )
        return items

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

route_name = 'item'

router = APIRouter(
    prefix=f'/{route_name}',
    tags=[route_name],
    # dependencies=[Depends(auth.get_current_user)],
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

@router.get("")
# @router.get("", response_model = List[Union[User,Item]])
# def read_items(current_user: User = Depends(auth.get_current_user)):
async def read_items(current_user: User = Depends(auth.get_current_user)):

    current_user = User(**current_user)
    print(current_user)

    items = Item.GetItems(current_user.ID)

    print(f'items found: ({len(items)})')

    # items.insert(0, current_user)
    # return items

    return [current_user, *items]

@router.post("/create")
# def read_items(new_item: Item, current_user: User = Depends(auth.get_current_user)):
async def create_item(new_item: Item, current_user: User = Depends(auth.get_current_user)):

    current_user = User(**current_user)
    return Item.GetItems(current_user.ID)



#In[]

if __name__ == '__main__':
    quit(0)