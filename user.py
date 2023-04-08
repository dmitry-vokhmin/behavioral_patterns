from observer import Observer


class User(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, *args):
        print(f"User {self.name} received message: {args}")
