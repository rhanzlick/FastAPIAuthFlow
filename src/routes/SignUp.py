import sys, datetime
from typing import Annotated, List, Union, Dict

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse

from ..models.Authenticator import Authenticator

route_name = 'signup'

Router = APIRouter(
    prefix=f'/{route_name}',
    tags=[route_name],
    # dependencies=Depends(),
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Page Not Found'},
    },
)

# @Router.get('/')
# async def GetSignUpPage():
#     pass

@Router.post('/')
async def UserSignup(req: Request):
    pass

# class Router():
#     route_name = 'sign-up'
#     def __init__(self) -> None:
#         pass
    
#     @staticmethod
#     def GetRouter():
#         route = APIRouter(
#             prefix=f'/{Router.route_name}',
#             tags=[Router.route_name],
#             # dependencies=Depends(),
#             responses={
#                 401: {'description': 'Unauthorized'},
#                 404: {'description': 'Page Not Found'},
#             },
#         )
        
#         @route.get('/')
#         async def GetSignUpPage():
#             return {'hello':'get signup page'}

#         return route

# if __name__ == '__main__':
#     sys.exit()

