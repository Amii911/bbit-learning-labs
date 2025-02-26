#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
class securityInterface():
    def __init__(self, name: str) -> None:
        self.setName(name)

    def setName(self, name) -> str:
        self.name = name
    
    def getName(self) -> str:
        return self.name

class security(securityInterface):
    pass
