from Person import Person

class Client(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)

    
