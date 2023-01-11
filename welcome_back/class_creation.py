class NewClass:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name: str):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_age(self, age: int):
        self.age = age

    def get_age(self):
        return self.age


felix = NewClass("Din", "Ezeike", 20)
felix.set_first_name("Felizdujadin")
felix.get_first_name()
print(felix.get_first_name())
