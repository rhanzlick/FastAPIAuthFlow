import jwt
import datetime
from datetime import timedelta
import jwt.algorithms
from pydantic import BaseModel
# from src.models.User import User

secret_key = '83d0f3d08f5fc04e254af1ba050c981c766f866f4061bde31fabfc1e4a6ec7bd'
algo = 'HS256'

class Token(BaseModel):

    username:str
    expiration:datetime.datetime
    # expire_duration:float = 30

    @staticmethod
    # def Encode(user:User):
    def Encode(user:dict, expire_duration:float = 30):
        expiry = datetime.datetime.now(datetime.timezone.utc) + timedelta(minutes = expire_duration)
        payload = {
            'user_id': user.get('username'),
            'exp': expiry,
        }

        return jwt.encode(
            payload,
            key = secret_key,
            algorithm = algo,
        )

    @staticmethod
    def Decode(token:str):

        decoded = jwt.decode(
            token,
            secret_key,
            algorithms = algo,
        )

        dt = datetime.datetime.fromtimestamp(decoded.get('exp'))

        return Token(
            username = decoded.get('user_id'),
            # expiration = decoded.get('exp'),
            expiration = dt,
        )