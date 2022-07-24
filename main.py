from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


class InputFromUserModel(BaseModel):
  name: str;
  age: int;

app = FastAPI()
indexHTML = FileResponse('public/index.html')

@app.get('/')
async def index():
  return indexHTML

@app.get('/welcome')
async def welcome():
  return 'Welcome!'

@app.get('/data')
async def sample_date():
  return { 'data': [] }

@app.post('/input')
async def input_from_user(data: InputFromUserModel):
  print(data);
  return 'complete input'