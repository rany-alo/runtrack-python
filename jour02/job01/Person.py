class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def get_firstname(self):
        return self.firstname

    def set_firstname(self, new_firstname):
        self.firstname = new_firstname
    
    def get_lastname(self):
        return self.lastname

    def set_lastname(self, new_lastname):
        self.lastname = new_lastname
    
    def sePresenter(self):
        print(f"{self.firstname} {self.lastname}")