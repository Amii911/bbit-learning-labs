#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
class securityInterface():
    def __init__(self, name: str) -> None:
        self.name = name

    def setName(self, name) -> str:
        self.name = name
    
    def getName(self) -> str:
        return self.name

class security(securityInterface):
    def __str__(self) -> str:
        return f"Security Name: {self.getName()}"
