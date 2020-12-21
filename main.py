import cashRegister as CashRegister
import controlInventory as ControlInventory
from inputControl import classBecauseINeedToTurnTheseIntoMethodsForSomeReason
from datetime import datetime
from pytz import timezone
from fileHandler import handleFile

inputClass = classBecauseINeedToTurnTheseIntoMethodsForSomeReason()
#Instantiate input control class
handler = handleFile()
#Instantiate file handler class

def getDate():
    #Define getDate() function
    e = datetime.today().strftime('%Y-%m-%d')
    return e

def write(nameOfFile):
    print('Creating new text file') 

    name = 'inventory.'+nameOfFile+'.txt'  # Name of text file coerced with +.txt

    file = open(name,'w+')   # Trying to create a new file or open one
    return file, name

class master:
    #Define master class
    def __init__(self, inpList):
        #Define __init__() method
        self.inventory = inpList
        #Define self.inventory as inpList asgument
    #endmethod
#endclass
        
def main():
    #Define main() function
    masterList = master(handler.returnAll())
    #Instantiate master class with returnAll() function from file handler class(entire contents of the inventory.txt file)
    e = 0
    #Define e as 0
    while e < 1:

        inp = inputClass.createMenu("Welcome to Jaden's POS! Which of the following would you like to select: ", "Inventory control", "Cash register", "Exit", "Save inventory file")
        #Create selection menu
        if inp == "1":
            #If user selects 1
            masterList = ControlInventory.InventoryControl(masterList).inventoryMenu()
            #Redefine masterList while calling inventoryMenu() method from InventoryControl class
        elif inp == "2":
            #If user selects 2
            masterList = CashRegister.CashRegister(masterList).checkout()
            #Redefine masterList while calling checkout() method from CashRegister class
        elif inp == "3":
            #If user selects 3
            print("Goodbye!")
            #Print message to user
            e += 1
            #Break loop
        elif inp == "4":
            #If user selects 4
            d = getDate()
            a = write(d)
            datStr = a[1]
            for u in masterList.inventory:
                handler.addSpecLine(u, datStr)
        #endif
    #endwhile
#endfunction

main()
#Call to main() function