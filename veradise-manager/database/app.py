import uuid
import os
import conf as CONFIG
import info as INFO

class Database:
    def __init__(self):
        self.id = ""
        self.db_name = ""
        self.db_list = []

    def get_db_name(self):
        return self.db_name

    def get_id(self):
        return self.id

    def _create(self):
        location = CONFIG.MAIN_PATH + f"/{INFO.CONTAINER_NAME}"
        path_location = location + f"/{self.id}"
        if os.path.exists(path_location):
            print("Database already exists.")
            return
        else:
            os.makedirs(path_location)
            open(path_location + "/" + self.db_name, 'a').close()
            print("Database is created.")
            return

    def create(self, db_name):
        self.id = uuid.uuid4().hex
        self.db_name = db_name.lower()
        self._create()