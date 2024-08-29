from typing import Any, Dict, List, Union
from fastapi import HTTPException
from .User import User
import uuid

class Database():

    def __init__(self) -> None:
        self.Users:Dict = {}
        self.Sessions:Dict[str, str] = {}

    def HashPass(self, raw_pass:str) -> str:
        return f'hashed_{raw_pass}'
    
    async def GetUser(self, username:str, password:str) -> User:
        if username in self.Users:
            user = self.Users[username]
            if user['password'] == self.HashPass(password):
                return User(**user)
            else:
                HTTPException(403, 'Invalid username of password.')
    
    async def GetUserBySession(self, session_id:str) -> User:
        if session_id in self.Sessions:
            username = self.Sessions[session_id]
            return User(**self.Users[username])

    async def CreateUser(self, email:str, username:str, password:str) -> User:
        if username in self.Users:
            raise HTTPException(403, 'Username already exists.')
        hashed = self.HashPass(password)
        self.Users[username] = {
            'email':email,
            'username':username,
            'password': hashed
        }
        return User(email, username, hashed)
    
    async def CreateSession(self, user:User) -> str:
        existing_session = [s for s in self.Sessions.items() if s[1] == user.username]
        if existing_session is None:
            session_id = str(uuid.uuid4())
            self.Sessions[session_id] = user.username
            return session_id
        return existing_session[0]

db = Database()

def get_db() -> Database:
    if db is None:
        db = Database()
    return db
