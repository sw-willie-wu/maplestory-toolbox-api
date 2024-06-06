import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

class Validator:
    
    @staticmethod
    def valid_admin(self, credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
        admin = secrets.compare_digest(credentials.username, )
        password = secrets.compare_digest(credentials.password, )
        
        if not (admin and password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )

        return credentials.username