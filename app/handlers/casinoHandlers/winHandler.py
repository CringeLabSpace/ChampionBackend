from fastapi import HTTPException
from main import app
from database import query
from app.utils import format_current_time


async def win_handler(user_id: int, win_amount: int):
    player_row = await query('SELECT credit FROM players WHERE playerId = ?', (user_id))
    player_row = player_row[0] if player_row else None


    if not player_row:
        raise HTTPException(status_code=404, detail='Player not found')


    new_credit = player_row['credit'] + win_amount
    await query('UPDATE players SET credit = ? WHERE playerId = ?', (new_credit, user_id))


    result = {
        'credit': new_credit,
        'result': 1,
        'time': format_current_time()
    }


    return result


@app.post('/win')
async def win_route(data: dict):
    try:
        user_id = data['id']
        win_amount = data['win']
        return await win_handler(user_id, win_amount)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))