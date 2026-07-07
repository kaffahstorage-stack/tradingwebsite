"""Minimal backend stub — Trading Command Center is a fully static frontend app.
This exists only to keep supervisor's `backend` service healthy."""
from fastapi import FastAPI

app = FastAPI(title="Trading Command Center Stub")


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "trading-command-center-stub"}
