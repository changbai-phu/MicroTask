import sqlite3


class DatabaseManager:
    def __init__(self, db_name="mydatabase.db"):
        self.db_name = db_name

    def connect_db(self):
        return sqlite3.connect(self.db_name)
    
    def create_table(self):
        """Create users table if it does not exist"""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pomodoro_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            start_time TEXT,
            end_time TEXT,
            note TEXT,
            FOREIGN KEY(task_id) REFERENCES tasks(id)
            )
        """)
        conn.commit()
        conn.close()
    
class SessionManager:
    def __init__(self, db_name="mydatabase.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def insert_user(self, name, age):
        """Insert a new user into the database"""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        conn.close()
