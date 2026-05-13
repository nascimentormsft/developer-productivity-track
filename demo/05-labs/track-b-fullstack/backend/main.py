"""
Track B: Full-Stack Application Lab — Backend API

A simple financial transactions API built with FastAPI.
Participants will use Agent mode to add features spanning multiple files.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.transactions import router as transactions_router

app = FastAPI(
    title="Financial Transactions API",
    description="Simple API for managing financial transactions",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions_router, prefix="/transactions", tags=["transactions"])


@app.get("/health")
def health_check():
    return {"status": "healthy"}
