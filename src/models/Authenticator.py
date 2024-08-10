import secrets, datetime, bcrypt
from typing import List, Dict
from .User import User

class Authenticator():

    def __init__(self) -> None:
        self.UserTable: List[User] = []
        self.SessionTable: Dict[str, str] = {}

    def CreateUser(self, user: User) -> bool:
        
        existing_user = next((u for u in self.UserTable if user.email == u.email or user.username == u.username))
        if existing_user is None:
            self.UserTable.append(user)
            return True
        else:
            return False

    def GetUser(self, email:str) -> User:

        return next((u for u in self.UserTable if u.email == email), None)
    
    def GetSessionUser(self, sessionId: str) -> User:

        if sessionId not in self.SessionTable:
            return None
        
        return self.GetUser(self.SessionTable[sessionId])
    
    @staticmethod
    def GetSessionId(size:int=256) -> str:

        return secrets.token_urlsafe(size)
    
    @staticmethod
    def EncryptPassword(plain_pass: str) -> str:
        return f'hashed|{plain_pass}'