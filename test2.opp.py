class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def publish(self):
        print(f"Публикация '{self.title}' написана {self.author}.")

    def info(self):  
        print(f"Публикация: {self.title} от {self.author}")

class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def read(self):
        print(f"Чтение книги '{self.title}' с {self.pages} страницами.")

    def info(self): 
        print(f"Книга: {self.title}, автор: {self.author}, страниц: {self.pages}")

class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def download(self):
        print(f"Скачивание электронной книги '{self.title}' размером {self.file_size} MB.")

    def info(self): 
        print(f"Электронная книга: {self.title}, автор: {self.author}, размер: {self.file_size} MB")

class Magazine:
    def __init__(self, title, issue):
        self.title = title
        self.issue = issue

    def info(self): 
        print(f"Журнал: {self.title}, номер выпуска: {self.issue}")

book = Book("Анна Каренина", "Лев Толстой", 864)
ebook = EBook("Война и мир", "Лев Толстой", 1225, 5)
magazine = Magazine("National Geographic", "August 2024")

# Полиморфизм с наследованием
book.info()
ebook.info()

# Полиморфизм без наследования
for publication in [ebook, book, magazine]:
    publication.info()  

magazine.info()    
