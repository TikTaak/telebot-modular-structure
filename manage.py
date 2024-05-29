import os
import colorama

from src.bot import Bot
from src.config import Config
from src.database.db import Database



# Load modules
def load_modules():
    modules = Config().modules.copy()
    # TODO: درواقع الان برنامه در فولدر ماژول ها میچرخد و ماژول ها را پیدا میکند ولی باید به ازای اسم ماژول ها در ستینگز جیسون ماژول ها به برنامه اضافه بشوند
    for filename in os.listdir('./src/modules'):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            if module_name in modules:
                print(colorama.Fore.GREEN + "Loading Module '{}'".format(module_name))
                module = __import__(f'src.modules.{module_name}', fromlist=[module_name])
                if hasattr(module, "module"):
                    module.module()
                modules.remove(module_name)
            else:
                raise Exception(
                    colorama.Fore.RED + "module '{}' not found".format(
                        module_name,
                    )
                )
        else:
            pass
    if modules:
        raise Exception(
            colorama.Fore.RED + "modules {} not found in modules folder".format(
                str(modules),
            )
        )



if __name__ == '__main__':
    print("Run Application ...")
    
    colorama.init(autoreset=True)
    
    # setup built in modules
    print(colorama.Fore.YELLOW + "Setup Bot")
    bot_instance: Bot = Bot()
    
    print(colorama.Fore.YELLOW + "Setup Config")
    config: Config = Config()
    
    print(colorama.Fore.YELLOW + "Setup Database")
    database: Database = Database()
    
    bot = bot_instance.bot
    
    print(colorama.Fore.YELLOW + "Loading modules ...")
    load_modules()

    print(colorama.Fore.GREEN + "Polling Started")
    bot.infinity_polling()


