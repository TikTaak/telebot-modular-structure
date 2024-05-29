import telebot

from functools import wraps
from src.bot import Bot

def module(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        bot_instance: Bot = Bot()    
        bot: telebot.TeleBot = bot_instance.bot
        func(bot)
    return wrapper_func
    