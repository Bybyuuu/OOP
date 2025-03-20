
import logging
import datetime

logging.basicConfig(
    filename="studio.log",
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат записи
    datefmt="%Y-%m-%d %H:%M:%S",  # Формат даты и времени
)

class Lk:

    def __init__(self, id, type, description=None):
        self.id = id
        self.type = type
        self.description = description
        logging.info(f"Создан объект Lk: id={id}, type={type}")

    def display_details(self):
        logging.info(f"Вызван метод display_details для объекта Lk: id={self.id}")
        print(f"ID: {self.id}")
        print(f"Type: {self.type}")
        if self.description:
            print(f"Description: {self.description}")


class Session(Lk):
   
    def __init__(self, id, client_id, photographer_id, date, time, description=None):
        super().__init__(id, "Session", description)
        self.client_id = client_id
        self.photographer_id = photographer_id
        self.date = date
        self.time = time
        logging.info(f"Создан объект Session: id={id}, client_id={client_id}, photographer_id={photographer_id}")

    def __str__(self):
        return f"Session ID: {self.id}, Client ID: {self.client_id}, Photographer ID: {self.photographer_id}, Date: {self.date}, Time: {self.time}, Description: {self.description}"

    def display_details(self):
        logging.info(f"Вызван метод display_details для объекта Session: id={self.id}")
        super().display_details()  
        print(f"ID клиента: {self.client_id}")
        print(f"ID фотографа: {self.photographer_id}")
        print(f"Дата: {self.date}")
        print(f"Время: {self.time}")


class Studio:
   

    MAX_SESSIONS = 50  # Максимальное количество сессий
    session_count = 0  # Текущее количество сессий

    def __init__(self, photographers):
        self.photographers = {p.id: p for p in photographers}  # Список в словарь
        self.clients = {}
        self.sessions = {}
        logging.info(f"Создан объект Studio с фотографами: {[p.id for p in photographers]}")

    def get_photographer_by_id(self, photographer_id):
       
        photographer = self.photographers.get(photographer_id)
        logging.info(f"Запрошен фотограф по ID: {photographer_id}.  Результат: {photographer.name if photographer else None}")
        return photographer

    def get_client_by_telegram_id(self, telegram_id):
       
        for client_id, client in self.clients.items():
            if hasattr(client, 'telegram_id') and client.telegram_id == telegram_id:  
                logging.info(f"Найден клиент по Telegram ID: {telegram_id}, id={client_id}")
                return client
        logging.info(f"Клиент с Telegram ID {telegram_id} не найден.")
        return None  # нельзя искать по telegram_id, нужно перебирать



class Photographer(Lk): 
    def __init__(self, id, name, studio_name, schedule, description=None):  
        super().__init__(id, "Photographer", description)  
        self.name = name  
        self.studio_name = studio_name
        self.schedule = schedule
        logging.info(f"Создан объект Photographer: id={id}, name={name}, studio={studio_name}")


class Client(Lk):
    def __init__(self, id, name, telegram_id, description=None):
        super().__init__(id, "Client", description)
        self.name = name
        self.telegram_id = telegram_id
        logging.info(f"Создан объект Client: id={id}, name={name}, telegram_id={telegram_id}")




photographer1 = Photographer(1, "Педро Хабибуллин", "зал1", "пн-пт")
photographer2 = Photographer(2, "Владимир Кораблев", "за2", "сб-вт")
photographer3 = Photographer(3, "Глеб Лисицын", "зал3", "ср-пт")


studio = Studio([photographer1, photographer2, photographer3])

client1 = Client(101, "Anna Smirnova", "anna_smirnova")
client2 = Client(102, "Петр Сидоров", "petr_sidorov")


studio.clients = {client1.id: client1, client2.id: client2}
logging.info(f"Добавлены клиенты в студию: {[c.id for c in studio.clients.values()]}")



session1 = Session(1, client1.id, photographer1.id, "2023-12-25", "10:00", "Новогодняя фотосессия")
# Лямбда-выражения для работы с сессиями

print_session_info = lambda session: print(f"Сессия ID: {session.id}, Дата: {session.date}")

# Лямбда для фильтрации сессий по ID фотографа
filter_sessions_by_photographer = lambda sessions, photographer_id: [
    s for s in sessions if s.photographer_id == photographer_id
]

# Лямбда для сортировки сессий по дате
sort_sessions_by_date = lambda sessions: sorted(sessions, key=lambda s: s.date)  

# Пример использования лямбда-выражений

print_session_info(session1)

sessions = [session1]

filtered_sessions = filter_sessions_by_photographer(sessions, 1)
print("\nСессии для фотографа с ID 1:")
for session in filtered_sessions:
    print(session)

# Сортируем сессии по дате
sorted_sessions = sort_sessions_by_date(sessions)
print("\nСессии, отсортированные по дате:")
for session in sorted_sessions:
    print(session)

logging.info("Программа завершена")
