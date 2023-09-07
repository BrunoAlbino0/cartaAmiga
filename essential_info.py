class UserInfo:

    def __init__(self, name: str, letters: List[Letter], relatives: List[Relatives]):
        self.name = name
        self.letters = letters
        self.relatives = relatives


class Letter:

    def __init__(self, sender: str, receiver: str, date: time, message: str):
        self.sender = sender
        self.receiver = receiver
        self.date = date
        self.message = message


class Relatives:

    def __init__(self, name: str, age: int, relation: str, letters: List[Letter]):
        self.name = name
        self.age = age
        self.relation = relation
        self.letters = letters
