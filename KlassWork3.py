class Student:
    def __init__(self, name, surname, age):
        self.__name = name
        self.surname = surname
        self.age = age


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            print("Имя должно быть строкой")
        else:
            self.__name = new_name.capitalize()



st1 = Student("Иван","Иванов", 19)
st1.name = "Петя"
print(st1.name)

