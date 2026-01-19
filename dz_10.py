import requests
import sqlite3
import time
from datetime import datetime


API_KEY = "ВСТАВ_СВІЙ_API_KEY"
CITY = "Chernihiv"
COUNTRY = "UA"
DB_NAME = "weather.db"
UPDATE_INTERVAL = 1800


class WeatherDatabase:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                datetime TEXT,
                temperature REAL
            )
        """)
        self.conn.commit()

    def insert_weather(self, dt: str, temp: float):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO weather (datetime, temperature) VALUES (?, ?)",
            (dt, temp)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()


def get_temperature() -> float:
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY},{COUNTRY}&appid={API_KEY}&units=metric"
    )
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["main"]["temp"]


def main():
    print("Запуск збору погоди. Для зупинки натисніть CTRL+C")
    db = WeatherDatabase(DB_NAME)

    try:
        while True:
            temperature = get_temperature()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            db.insert_weather(current_time, temperature)

            print(f"[{current_time}] Температура: {temperature} °C")
            time.sleep(UPDATE_INTERVAL)

    except KeyboardInterrupt:
        print("\nПрограму зупинено користувачем.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
