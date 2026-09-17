# server.py


from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import uvicorn


app = FastAPI()


zone_data = {"Zone 1": 45, "Zone 2": 60, "Zone 3": 50}


class Payload(BaseModel):

    zone: str
    density: int


@app.post('/api/ingest')
def ingest_data(payload: Payload):
    zone_data[payload.zone] = payload.density

    return {'status': 'success'}

@app.get('/api/status')
def get_status():

    return zone_data

@app.get('/')
def get_dashboard():
    with open('dashboard.html', 'r') as f:

        return HTMLResponse(content = f.read())


uvicorn.run(app, host = '0.0.0.0', port = 8000)
