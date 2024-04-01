from fastapi import HTTPException
from main import app
from database import query
from datetime import datetime


def format_current_time():
    current_date = datetime.now()
    formatted_time = current_date.strftime("%d-%m-%Y %H:%M:%S")
    return formatted_time


async def bet_handler(user_id: int, bet: int):
    player_row = await query('SELECT credit FROM players WHERE playerId = ?', (user_id))
    player_row = player_row[0] if player_row else None


    if not player_row:
        raise HTTPException(status_code=404, detail='Player not found')


    if player_row['credit'] < bet:
        result = {'credit': player_row['credit'], 'result': 0, 'time': format_current_time()}
    else:
        new_credit = player_row['credit'] - bet
        await query('UPDATE players SET credit = ? WHERE playerId = ?', (new_credit, user_id))
        result = {'credit': new_credit, 'result': 1, 'time': format_current_time()}


    return result


@app.post('/bet')
async def bet_route(date: dict):
    try:
        user_id = date['id']
        bet = date['bet']
        return await bet_handler(user_id, bet)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))