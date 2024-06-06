from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from router import api_router
# from service import Validator

app = FastAPI(
    version="0.1",
    debug=True,
    title='Maplestory Toolbox Api',
    docs_url=None, 
    redoc_url=None, 
    openapi_url = None
    # docs_url="/docs",
    # openapi_url="/openapi.json",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router
)


# import secrets
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# security = HTTPBasic()
# def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
#     correct_username = secrets.compare_digest(credentials.username, "user")
#     correct_password = secrets.compare_digest(credentials.password, "password")
#     if not (correct_username and correct_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return credentials.username