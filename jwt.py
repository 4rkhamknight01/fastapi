
##This file is for jwttoken related stuff so it creates a token valid for 30 minutes using the function create_access_token for a 
# user using it’s username and verify token is used for finding the current user which generated the token.
from datetime import datetime, timedelta
from jose import JWTError, jwt
import main

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
#using HS256 algorithm to encode the data using a secret key given above 

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
#this function creates an access token for the entered value wihch is valid for 30 minutes as stated above and encodes the JWT 
#with the secret key given above.

def verify_token(token:str,credentials_exception):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		username: str = payload.get("sub")
		if username is None:
			raise credentials_exception
		token_data = main.TokenData(username=username)
	except JWTError:
	    raise credentials_exception
#this function verifies whether the token that is being used in the session belons to the user or not i.e. 
#it verifies whether the user is legitimate or not. 
