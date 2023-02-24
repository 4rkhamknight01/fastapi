from fastapi import Depends,HTTPException
from jwt import verify_token
from fastapi.security import OAuth2PasswordBearer
import status

oauth2scheme = OAuth2PasswordBearer(tokenUrl="login")
# we are using OAuth2PasswordBearer to validate the current logged in user.

#function to find the current user that generated the token
def get_current_user(token:str = Depends(oauth2scheme)):
    credentials_exception = HTTPException(
        tatus_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate user", 
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token,credentials_exception)
#this functions finds the current user that generated the token when logging in.


