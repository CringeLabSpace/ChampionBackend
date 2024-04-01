from fastapi import FastAPI, HTTPException
from typing import Any

app = FastAPI()


def wallet_api(data: dict) -> Any:
    pass


def pay_callback_handler(data: dict) -> Any:
    pass


@app.post('/walletapi')
async def wallet_api_route(data: dict):
    try:
        return await wallet_api(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=3000)