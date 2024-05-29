import telebot
import os
from dotenv import load_dotenv
load_dotenv()



class Bot(object):
    """Singleton"""
    
    TOKEN: str = None
    bot: telebot.TeleBot = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Bot, cls).__new__(cls)
            cls.instance.setup()
        return cls.instance
    
    def setup(self) ->  None:
        self.TOKEN = os.getenv("TOKEN")
        self.bot = telebot.TeleBot(os.getenv("TOKEN"))
        return None
