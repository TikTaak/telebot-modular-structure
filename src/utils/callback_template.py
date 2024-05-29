import json
import telebot

def callback(prefix: str, data={}) -> str:
    res = {
        "prefix":prefix,
        "data": data
    }
    return str(res).replace("'", '"')

def prefix(call: telebot.types.CallbackQuery, prefix: str) -> bool:
    data = json.loads(
        call.data
    )
    
    return (
        data['prefix'] == prefix
    )