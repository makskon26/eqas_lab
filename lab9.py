class Conventor:
    def __init__(self):
        self.name = "film"

    def newVideo(self, film):
        self.name = film
        print(f"Завантажили відео {self.name}")

    def setupVideo(self):
        print(f"Конвертували відео {self.name} ")

    def uploadedVideo(self):
        print(f"Завантажили відео {self.name} на YouTube")

    def API(self):
        print("Отримали ключ з бази даних для YouTube")

    def digitalProcessing(self):
        print(f"Цифрова обробка та завантаження відео {self.name}")


class Facade:
    def __init__(self, convert):
        self.convert = convert

    def uploadedOnYouTube(self, name):
        self.convert.newVideo(name)
        self.convert.setupVideo()
        self.convert.uploadedVideo()

    def apiYouTube(self, name):
        self.convert.newVideo(name)
        self.convert.API()
        self.convert.digitalProcessing()


facade = Facade(Conventor())

facade.uploadedOnYouTube("Петро Щур Мамині світлиці.mp4")
print(' ')
facade.apiYouTube("Петро Щур Мамині світлиці.mp4")
