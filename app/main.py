from fastapi import FastAPI
from .routers import health, triage
app = FastAPI(title='VetCare+ API', version='0.1.0')
app.include_router(health.router, prefix='')
app.include_router(triage.router, prefix='/triage')
