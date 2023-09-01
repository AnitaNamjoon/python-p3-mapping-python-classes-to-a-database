from lib.config import CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)
        # Commit the changes to the database
        CURSOR.connection.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        # Get the last inserted row ID and assign it to the instance
        self.id = CURSOR.lastrowid
        # Commit the changes to the database
        CURSOR.connection.commit()

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
