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
jqueryfile = os.path.realpath('../Frontend/jquery.js')
loginfile = os.path.realpath('../templates/login/Login.html')
homefile = os.path.realpath('../templates/home/Home.html')
port = "80"
api = FastAPI(openapi_url=None,docs_url=None,redoc_url=None)

@api.get("/jquery")
async def jqueryfunc():
    global jqueryfile
    with open(jqueryfile) as f:
        content = f.read()
    content_type, _ = guess_type(jqueryfile)
    return Response(content, media_type=content_type)

@api.get("/check")
async def checkfunc(myvalue: str):
    print("Checking: "+myvalue)
    if 1==1:
        return {"Result": "Now"}
    else:
        return {"Result": "Wait"}

@api.get("/login")
async def displayfunc():
    with open(loginfile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

@api.get("/home")
async def displayfunc():
    with open(homefile, 'r') as temp6:
        temp4 = temp6.read()
    return HTMLResponse(temp4.replace("placeholderbody","replacing_is_working"))

host = "0.0.0.0"
api.add_middleware(CORSMiddleware,allow_origins="*".split(","),allow_methods=["*"],allow_headers=["*"])
uvicorn.run(api, host=host, port=int(port))
