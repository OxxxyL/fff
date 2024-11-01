import time
class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self): #Вывод инфо о пользователе
        return self.nickname

class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0 #Текущий тайм-код
        self.adult_mode = adult_mode #Режим для взрослых

    def __eq__(self, other): #Сравнение видео по заголовку
        return self.title == other.title

    def __contains__(self, item):  #Содержится ли строка в заголовке видео
        return item in self.title
class UrTube: #Платформа для видео
    def __init__(self):
        self.users = [] #Список пользователя
        self.videos = [] #Список видео
        self.current_user = None #Текущий пользователь

    def log_out(self): #Выход из аккаунта
        self.current_user = None

    def log_in(self, nickname: str, password: int): #Войти в аккаунт
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user #Проверка никнейма и пароля
                return

    def register(self, nickname: str, password: int, age: int): #Регистрация нового пользователя
        password = hash(password)
        for user in self.users: #Проверяет существует ли пользователь с таким никнеймом
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user #Добавляет нового пользователя в систему
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def add(self, *args):  #Добавляет видео на платформу
        for movie in args:
            if movie.title not in [video.title for video in self.videos]:
                self.videos.append(movie) #Проверка сущ. ли уже видео с таким заголовком

    def get_videos(self, text: str): #Поиск видео по заголовку
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie #Возвращает видео, где есть заданный текст

    def watch_video(self, movie: str): #Просмотр видео
        if self.current_user:
            for video in self.videos:
                if self.current_user and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return #Проверка возраста
                if movie in video.title: #Запуск видео с задержкой 1 секунды на каждую секунду видео
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')