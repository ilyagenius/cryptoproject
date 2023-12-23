from fastapi import APIRouter
import uvicorn

import asyncio
import aiohttp

import requests


api_router = APIRouter(prefix='/v1', tags=['v1'])

@api_router.get('/')
async def get_pair(pair: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pair}") as resp:
            return await resp.json()