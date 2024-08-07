class Client:
    def __init__(self,adress,persons,current,perv):
        self.adress = adress
        self.persons=persons
        self.current=current
        self.perv = perv

    def update_current(self,new_current):
        self.prev = self.current
        self.current = new_current

Client1 = Client("SDFS",4,35,20)
Client1.update_current(40)
print(Client1)