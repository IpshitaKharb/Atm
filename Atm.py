class Atm (object):
    def __init__(self,details) :
        self.details = details

    def check(self) :
         return f"Account: {self.name}"

Ipshita = Atm("NAME:Ipshita, ACCOUNT NUMBER:xyz, PIN:xxxxxx, BALANCE:infinty")
print(Ipshita.details)
