from starlette.responses import HTMLResponse
from fastapi import Request,FastAPI, File, UploadFile, Form, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Any, Dict, AnyStr, List, Union, Optional
import configparser
import base64
import os
from pathlib import Path
from mimetypes import guess_type
import sys


"""
just run this file and webserver will be started
"""

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]
jqueryfile = os.path.realpath('../templates/jquery.js')
loginfile = os.path.realpath('../templates/login/Login.html')
homefile = os.path.realpath('../templates/home/Home.html')
loan_amount = os.path.realpath('../templates/home/Home.html')
balance = os.path.realpath('../templates/home/Home.html')
signup = os.path.realpath('../templates/register/Register.html')
# basefile = os.path.realpath('../templates/base.html')
# indexfile = os.path.realpath('../templates/index.html')
landingfile = os.path.realpath('../templates/landing/index.html')

# profilefile = os.path.realpath('../templates/profile.html')

# signupfile = os.path.realpath('../templates/signup.html')


port = "80"
api = FastAPI(openapi_url=None,docs_url=None,redoc_url=None)

@api.get("/jquery")
async def jqueryfunc():
    global jqueryfile
    with open(jqueryfile) as f:
        content = f.read()
    content_type, _ = guess_type(jqueryfile)
    return Response(content, media_type=content_type)

@api.get("/signup")
async def signupfunc():
    with open(signup, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

@api.get("/landing")
async def landingfilefunc():
    with open(landingfile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))



## to check the login info
@api.get("/check")
async def checkfunc(myvalue: str):
    print("Checking: "+check)
    email, password = myvalue.split(",")
    check_email = calldb("login", email)
    check_password = calldb("login", password)
    if email != check_email and password != check_password:
        return print("Please try again as your login information is wrong. ")
    else :
        homefunc("/home")

    if 1==1:
        return {"Result": "Now"}
    else:
        return {"Result": "Wait"}

## login endpoint to display
@api.get("/login")
async def loginfunc():
    with open(loginfile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))


@api.get("/home")
async def homefunc():

    with open(homefile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

@api.get("/loan_amount")
async def loan_amountfunc():

    with open(loan_amount, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

@api.get("/balance")
async def balancefunc():
    with open(balance, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

@api.get("/base")
async def basefunc():
    with open(basefile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

@api.get("/index")
async def indexfunc():
    with open(indexfile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

@api.get("/profile")
async def profilefunc():
    with open(profilefile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

@api.get("/logout")
async def logoutfunc():
    with open(logoutfile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))


host = "0.0.0.0"
api.add_middleware(CORSMiddleware,allow_origins="*".split(","),allow_methods=["*"],allow_headers=["*"])
uvicorn.run(api, host=host, port=int(port))
