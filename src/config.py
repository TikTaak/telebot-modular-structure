import json


class Config(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
            cls.instance.setup()
        return cls.instance
    
    def setup(self) ->  None:
        config_file = open("settings.json")
        config_data: dict = json.loads(
            config_file.read()
        )
        for key in config_data:
            setattr(self, key, config_data[key])
        
        return None
    
