import uuid, secrets, asyncio
from typing import Annotated, List, Union

from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
# from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
# from starlette.staticfiles import StaticFiles
# from starlette.responses import RedirectResponse
# from starlette.templating import Jinja2Templates


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# templates = Jinja2Templates(directory='src/templates')

# from models.User import User
# from models.Authenticator import Authenticator

#from routes.Pages import Router as PageRouter
from routes.User import Router as UserRoutuer
#from routes.SignUp import Router as SignUpRouter


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=[''],
    allow_methods=['*'],
    allow_headers=['*'])

# app.mount('/src/static', StaticFiles(directory='src/static'), name="static")

@app.get('/')
async def root():
    
    return {'routes':', '.join([str(r.path) for r in app.routes])}

app.include_router(UserRoutuer)
# app.include_router(PageRouter)
#app.include_router(SignUpRouter)


if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("src.index:app", host="0.0.0.0", port=8_000, reload=True)
    uvicorn.run("index:app", host="0.0.0.0", port=8_000, reload=True)

