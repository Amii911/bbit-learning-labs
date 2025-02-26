#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
# Allow for a position to be created with a security name or object and a seed position value
# Allow for gathering of the position's security and position value
# Allow for updating of the position's size via addition & setting
from implementations.securitySolution import securityInterface

class positionInterface():
    def __init__(self, security, initialPosition: int) -> None:
        self.positionValue = initialPosition
        
        if type(security) == str:
            self.security = securityInterface(security)
        else:
            self.security = security
    
    def getSecurity(self) -> securityInterface:
        return self.security

    def getPosition(self) -> int:
        return self.positionValue
    
    def setPosition(self, inputValue: int) -> None:
        # if inputValue < 0: 
        #     raise Exception("")
        self.positionValue = inputValue 
                
    
    def addPosition(self, inputValue: int) -> None:
        if self.positionValue + inputValue < 0: 
            raise Exception("")
        self.positionValue += inputValue
              
class position(positionInterface):
    pass
