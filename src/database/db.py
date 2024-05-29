import sqlite3


class Database(object):
    db = None
    cursor = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance' ):
            cls.instance = super(Database, cls).__new__(cls)
            cls.instance.setup()
        return cls.instance
    
    def setup(self) -> None:
        self.db = sqlite3.connect("data/db.sqlite3")
        self.cursor = self.db.cursor()        
        self.cursor.execute('')
        self.db.commit()
        
        return None