import uuid, secrets, asyncio
from typing import Annotated, List, Union

from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
#from starlette.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates

from .routes.SignUp import Router as SignUpRouter
from .models.User import User

templates = Jinja2Templates(directory='src/templates')

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_credentials=True,
#     allow_origins=[''],
#     allow_methods=['*'],
#     allow_headers=['*'])

app.mount('/src/static', StaticFiles(directory='src/static'), name="static")
app.include_router(SignUpRouter)


@app.get('/')
async def root():
    return {'hello':'index1'}

@SignUpRouter.get('/')
async def SignUpPage(req:Request):
    context = {
        'request':req,
    }
    return templates.TemplateResponse('signup.html', context)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.index:app", host="0.0.0.0", port=8_000, reload=True)

