# /// script
# dependencies = [
#     'fastapi[standard]',
#     'uvicorn',
#     'pandas',
#     'requests'
# ]
# ///

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
import requests
import os
import uvicorn

#from routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(router, prefix="/api/v1")

@app.get("/", response_class=JSONResponse)
async def root():
    return {"message": "Hello World!"}

@app.get("/more", response_class=PlainTextResponse)
async def root(class_: str = Query(..., alias="class")):
    return f"Hello {class_}"

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)