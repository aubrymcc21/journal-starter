from prometheus_client import Counter, generate_latest
from fastapi import FastAPI, Request
from fastapi.responses import Response
from prometheus_fastapi_instrumentator import Instrumentator
from dotenv import load_dotenv
from api.controllers import journal_router
import logging

load_dotenv()

app = FastAPI()
app.include_router(journal_router)

logging.basicConfig(filename='myapp.log', level=logging.INFO)


Instrumentator().instrument(app).expose(app)