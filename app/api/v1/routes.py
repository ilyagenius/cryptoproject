import uvicorn
import asyncio
import threading
import websockets
import json
import asyncio
import aiohttp

from fastapi import APIRouter
from app.db.utils import get_last_rate, get_rate_from_time
from datetime import datetime


api_router = APIRouter(prefix='/v1', tags=['v1'])


@api_router.get('/')
async def get_pair(pair: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pair}") as resp:
            return await resp.json()
        

@api_router.get('/p')
async def get_pair_last_rate(pair: str):
    return await get_last_rate(pair)

@api_router.get('/pp')
async def get_rate_from_time(
    start_time: datetime,
    end_time: datetime,
    pair: str):
    return await get_rate_from_time(start_time, end_time, pair)
