import json
import telebot

from src.bot import Bot
from src.config import Config
from src.utils.module_decorator import module
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from src.utils.callback_template import callback, prefix



class Markup:
    @staticmethod
    def markup_test() -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        
        # do stuff
        temp = "salam"
        
        markup.add(
            InlineKeyboardButton(
                text="Button 1",
                callback_data=callback(prefix="button_1", data={"name":temp})
            )
        )
        return markup

@module
def module(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message: telebot.types.Message):
        bot.send_message(
            chat_id=message.chat.id,
            text="منو اصلی".format(message.chat.id),
            reply_markup=Markup.markup_test()
        )
        
    @bot.message_handler(func=lambda message: True)
    def message_handler(message: telebot.types.Message):
        bot.send_message(
            chat_id=message.chat.id,
            text="آی دی عددی چت {} میباشد".format(message.chat.id),
            reply_markup=Markup.markup_test()
        )
        
    @bot.callback_query_handler(func=lambda call: prefix(call, "button_1"))
    def callback_query(call: telebot.types.CallbackQuery):
        if Config().debug:
            print(call.data)    
        data: dict = json.loads(call.data)['data']
        
        # do stuff
        print("stuff")        
        
        
        bot.answer_callback_query(call.id)

            