from prometheus_client import Counter, generate_latest
from fastapi import FastAPI, Request
from fastapi.responses import Response
from dotenv import load_dotenv
from api.controllers import journal_router
import logging

load_dotenv()

# TODO: Setup basic console logging
# Hint: Use logging.basicConfig() with level=logging.INFO

app = FastAPI()
app.include_router(journal_router)

logging.basicConfig(filename='myapp.log', level=logging.INFO)


REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests", ["method", "endpoint"])

@app.middleware("http")
async def count_requests(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    return response

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
