from fastapi import FastAPI
import uvicorn

from .api.v1 import routes


app = FastAPI()
app.include_router(routes.api_router, prefix="/api")


if __name__ == '__main__':
    uvicorn.run('app.app:app', host="0.0.0.0", port=8000)