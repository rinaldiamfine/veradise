import database
import conf as CONFIG
import info as INFO
import os
import glob

class Manager:
    def __init__(self, args):
        self.args = args
        self.setupContainer()
        self.run()
        pass

    def setupContainer(self):
        if not os.path.exists(CONFIG.MAIN_PATH):
            os.makedirs(CONFIG.MAIN_PATH + f"/{INFO.CONTAINER_NAME}")

    def create(self):
        command = self.args[2]
        if command.lower() == "database":
            name = self.args[3] if len(self.args) > 3 else None
            if name:
                db = database.app.Database()
                try:
                    db.create(name)
                except Exception as e:
                    print(f"Failed to create database: {e}")
                    return
            else:
                print("Please specify a database name.")
                return

        elif command.lower() == "table":
            print("Create Table")
        else:
            print("Unknown command.")
            return

    def read(self):
        command = self.args[2]
        if command.lower() == "database":
            db = database.app.Database()
            path_location = glob.glob(CONFIG.MAIN_PATH + f"/{INFO.CONTAINER_NAME}/*")
            for db_path in path_location:
                db_id = db_path.split("/")[-1]
                db_name = filter(lambda name: name not in CONFIG.DB_STRUCTURE, os.listdir(db_path))
                format_db = {
                    "id": db_id,
                    "name": list(db_name)[0]
                }
                db.db_list.append(format_db)
            print(db.db_list, "GET ALL DB LIST")
            
        elif command.lower() == "table":
            print("Show Table")
        else:
            print("Unknown command.")
            return
    
    def delete(self):
        print("Delete")
        command = self.args[2]
        if command.lower() == "database":
            print("Delete Database")
        elif command.lower() == "table":
            print("Delete Table")
        else:
            print("Unknown command.")
            return

    def run(self):
        if len(self.args) <= 1:
            print("Please specify a command.")
            return
        else:
            command = self.args[1]
            if command.lower() == "create":
                self.create()
            elif command.lower() == "delete":
                self.delete()
            elif command.lower() == 'show':
                self.read()
            elif command.lower() == "info":
                print(f"App name: {INFO.APP_NAME} \nContainer name: {INFO.CONTAINER_NAME} \nVersion: {INFO.VERSION} \nPath: {CONFIG.MAIN_PATH}")
            else:
                print("Unknown command.")
                return