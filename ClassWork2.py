import time


class Blog:
    def __int__(self):
        self.name = name
        self.author = author
        self.posts = posts

    def make_post(self, post):
        post = {}
        post["text"] = text
        t = time.localtime()
        post["time"] = time.strftime("%H:%M:%S",t)
        self.posts.append(post)

    def delete_post(self):
        for i in self.posts:
            if i["title"] == title:
                self.posts.remove(i)
        else: print(f"Поста с заголовком {title} не существует")


blog = Blog("Питон", "Лукьянов")
while True:
    choice = input("Вы можете: \n1. Создать пост\n2. Удалить пост\nВаш выбор")
    match choice:
        case "1":
            title = input("Введите заголовок: ")
            text = input("Введите текст: ")
            blog.make_post(title)
            print(blog)
        case "2":
            title
        case _: