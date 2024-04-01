from fastapi import HTTPException
from main import app
from database import query
from datetime import datetime


def format_current_time():
    current_date = datetime.now()
    formatted_time = current_date.strftime("%d-%m-%Y %H:%M:%S")
    return formatted_time


async def cancel_handler(user_id: int):
    player_row = await query('SELECT credit FROM players WHERE playerId = ?', (user_id,))
    player_row = player_row[0] if player_row else None

    if not player_row:
        raise HTTPException(status_code=404, detail='Player not found')

    return {
        'credit': player_row['credit'],
        'player_id': user_id,
        'result': 1,
        'time': format_current_time(),
        'currency': 'XYR'
    }


@app.post('/cancel')
async def cancel_route(data: dict):
    try:
        user_id = data['id']
        return await cancel_handler(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))