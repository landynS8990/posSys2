from inputControl import classBecauseINeedToTurnTheseIntoMethodsForSomeReason
#Import ibput control class
from fileHandler import handleFile
#Import file handler class
inputClass = classBecauseINeedToTurnTheseIntoMethodsForSomeReason()
#Instantiate input control class
handler = handleFile()
#Instantiate file handler class
class CashRegister:
    #Define cash register class
    def __init__(self, masterList):
        #init method with masterList argument
        self.masterList = masterList
        #Define masterList as masterList argument
        print(self.masterList.inventory)
        #Print inventory list
    #endmethod
    def checkout(self):
        #Function for user to make purchase at checkout
        self.purchases = []
        #Define purchases list
        self.getShoppingList()
        #Call getShoppingList() method
        mainTotal = 0
        #Define subtotal price
        nameAmList = []
        #Define list for name and amount
        priceAndList = []
        #Define list for prices of individual items
        for i in self.purchases:
            #Loop through purchases list
            nameAmList += [(i.strPrint()[0]) + (i.strPrint()[1])]
            #Add name and amount of each item to name and amount list
            priceAndList += [i.strPrint()[2]]
            #Add item price to item price list
            mainTotal += float(i.strPrint()[2])
            #Add item price to subtotal
        #endfor
        snips = wesleySnipesWorstNightmare(mainTotal).returnTax()
        #Call tax class returnTax() method to get tax price and full total
        u = paymentType(snips[1]).handlePayMent()
        #Call to paymentType class handlePayment() method to get payment method and change due
        rec = handleReciept(nameAmList, priceAndList, mainTotal, snips[0], snips[1], u[0], u[1]).finalPrint()
        #Call to handleReciept class finalPrint() method to print reciept
        print(rec)
        #Print reciept
        input("\nPress Enter To Continue\t")
        #get user input
        return self.masterList
        #Return masterList to update masterList in main() after transaction
    #endmethod

    def getShoppingList(self):
        #Define getShoppingList() method
        ks = 0
        #Define ks as 0
        while ks < 1:
            #While ks is less than 1
            userInput = inputClass.createMenu("Would You Like To Purchase Another Item", "Yes", "No")
            #Create menu and get user input
            if userInput == "1":
                #if user selects yes
                self.getItem()
                #Call to getItem() method
                self.itemAmount = inputClass.getIntOnly(f"How many {self.currentItem[1]}s would you like to buy?:   ")
                #Get user int input for how many they'd like to buy
                if self.itemAmount < int(self.currentItem[4]):
                    self.purchases.append(Purchase(self.currentItem, self.itemAmount ))
                else:
                    currStock = int(self.currentItem[3]) - int(self.currentItem[4])
                    print(f"Please buy less than {currStock}")
                #Append item to purchases list
                r = 0
                for j in self.masterList.inventory:
                    if j[0] in self.masterList.inventory[r][0]:
                        amn = int(self.masterList.inventory[r][3]) - self.itemAmount
                        self.masterList.inventory[r][3] = str(amn)
                        newStr = ""
                        for n in self.masterList.inventory[r]:
                            newStr += f"{n} "
                        newStr += '\n'
                        handler.replace_line(self.masterList.inventory[r][0], newStr)
                    r += 1
            else:
                #If user selects no
                ks += 1
                #Break loop
            #endif
        #endwhile
    #endmethod
    def getSpecificItem(self, query):
        #Define getSpecificItem() method for user to select which item they'd like to buy and how much of said item they want
        l = 0
        #Define l as 0
        mainThing = []
        searchQuery = query
        #Get search query
        for t in self.masterList.inventory:
            #Loop through inventory list
            print(t[0])
            #Print current product SKU
            if searchQuery.lower() in t[0].lower():
                #If searchQuery is in current SKU
                l += 1
                #Add 1 to l
                print("Your query returned:   ")
                print(t)
                #Print message to user
                return t
                #Return product
        if l == 0:
            #if l is still 0(no matching products were found)
            print("Item not found. Please ensure you typed it correctly")
            #Print message to user
            return
            #Return nothing

    def getItem(self):
        #Define getItem() method
        self.currentItem = None
        #Define self.currentItem as None
        while self.currentItem is None:
            #While self.currentItem is none(No item matching user input has been found)
            self.currentItem = self.getSpecificItem(input("Please Enter the SKU of the item:    "))
            #Call to getSpecificItem method(returns none if no matching products are found)
            #if matching product is found, breaks loop
        #endwhile
        return self.currentItem
        #Return currentItem
    #endmethod
#endclass

class Purchase:
    #Define purchase class
    def __init__(self, item, amount):
        #Definit __init__() method
        self.item = item
        #Define self.item as item argument
        self.amount = amount
        #Define self.amount as amount argument
        self.totalPrice = float(self.item[7]) * self.amount
        #Define totalPrice as item price(index 7 of item list) times the amount of the item purchased
    #endmethod

    def strPrint(self):
        #Define strPrint() method to return name and amount of the item in question
        nameAndAmount = f"{self.amount: <5}{self.item[1][:20] + ':': <20}"
        #Define nameAndAmount as f string of amount and item name right-centered
        priceAndTotal = f"{self.item[7]: >7}{self.totalPrice: >7}"
        #Define priceAndTotal as f string of individual item price and totalPrice left-centered
        return nameAndAmount, priceAndTotal, self.totalPrice
        #Return nameAndAmount, priceAndTotal and user subTotal
    #endmethod
#endclass

class wesleySnipesWorstNightmare:
    #Define tax class
    def __init__(self, subTotal):
        #Define __init__() method
        self.subTotal = subTotal
        #Define self.subTotal as subTotal argumenr
    #endmethod

    def returnTax(self):
        #Define returnTax method
        taxed = self.subTotal * 0.13
        #Define tax amount as subTotal * 13%(purchase tax in Canada)
        totalTaxes = self.subTotal * 1.13
        #Define final total as subTotal * 113%
        return taxed, totalTaxes
        #Return tax amount and final total
    #endmethod
#endclass
    
class paymentType:
    #Define paymentType class
    def __init__(self, amountGiven):
        #Define __init__() method
        self.amountGiven = amountGiven
        #Define amountGiven as amountGiven argument
        self.method = ""
        #Define self.method as empty string for now
    #endmethod

    def selectPayment(self):
        #Define selectPayment() method
        pey = inputClass.createMenu("How would you like to pay?", "Cash", "Credit card", "Debit card")
        #Create menu for user input
        if pey == "1":
            #If user selects 1(Cash)
            self.method = "Cash"
            #Define self.method as Cash
            return self.method
            #Return self.method
        elif pey == "2":
            #If user selects 2(Credit card)
            self.method = "Credit card"
            #Define self.method as Credit card
            return self.method
            #Return self.method
        else:
            #If otherwise(user selects 3)
            self.method = "Debit card"
            #Define self.method as Debit card
            return self.method
            #Return self.method
        #endif
    #endmethod
    def handlePayMent(self):
        #Define handlePayment() method
        u = 0
        #Define u as 0
        totalAmnt = 0.0
        #Define totalAmount as 0
        while u < 1:
            #While u is less than 1
            inp = inputClass.getFloatOnly(f"How much are you paying?(total ${self.amountGiven}):    ")
            #Get user input for how much they've paid
            totalAmnt += inp
            #Add user input to totalAmnt
            if totalAmnt < self.amountGiven:
                #if user paid less than the reciept total
                print(f"So far you've paid ${totalAmnt}")
                #Print message to user
            elif totalAmnt >= self.amountGiven:
                #if user paid more than or as much as the reciept total
                u += 1
                #Break loop
                change = totalAmnt - self.amountGiven
                #Calculate change as amount paid minus reciept total
                pay = self.selectPayment()
                #Call to selectPayment method
                return pay, change
                #Return payment method and change due
            #endif
        #endwhile
    #endmethod
#endclass

class handleReciept:
    #Define handleReciept class
    def __init__(self, nameAndAmountList, priceList, subTotal, taxAmount, taxTotal, payMethod, change):
        #Define __init__() method
        self.nameAndAmount = nameAndAmountList
        self.priceList = priceList
        self.subTotal = subTotal
        self.taxAmount = taxAmount
        self.taxTotal = taxTotal
        self.payMethod = payMethod
        self.change = change
        #Define attributes of reciept as given arguments
    #endmethod
    def nameAmnt(self):
        #Define nameAmnt() method
        for i in self.nameAndAmount:
            #Loop through nameAndAmount list given
            print(f"{i}\n")
            #Print each individual item in the list
        #endfor
    #endmethod
    def priceAmnt(self):
        #Define priceAmnt() method
        s = len("Subtotal:")
        #Get length of first string
        t = len("Tax:")
        #Get length of second string
        tt = len("Total:")
        #Get length of third string
        firstNumb = (40 - (s + len(str(self.subTotal))))
        secondNumb = (40 - (t + len(str(self.taxAmount))))
        thirdNumb = (40 - (tt + len(str(self.taxTotal))))
        #Find out number of spaces needed in the reciept by subtrcting 40(maximum characters per line) by the length of all other strings in each line
        firstZero = " " * firstNumb
        secondZero = " " * secondNumb
        thirdZero = " " * thirdNumb
        #Create the space string by multiplying a single character space string by how many spaces are needed for each line
        print(f"SubTotal:{firstZero}{self.subTotal}")
        print(f"Tax:{secondZero}{self.taxAmount}")
        print(f"Total:{thirdZero}{self.taxTotal}")
        #Print each line with the description, the string of spaces and the main value of the line
    #endmethod
    def debitAmnt(self):
        #Define debitAmnt() method
        s = len(f"{self.payMethod}:")
        #Get length of first string
        t = len("Amount due:")
        #Get length of second string
        firstNumb = (40 - (s + len(f"-{self.taxTotal}")))
        secondNumb = (40 - (t + len(str(self.change))))
        #Find out number of spaces needed in the reciept by subtrcting 40(maximum characters per line) by the length of all other strings in each line
        firstZero = " " * firstNumb
        secondZero = " " * secondNumb
        #Create the space string by multiplying a single character space string by how many spaces are needed for each line
        print(f"{self.payMethod}:{firstZero}{self.taxTotal}")
        print(f"Amount due:{secondZero}{self.change}")
        #Print each line with the description, the string of spaces and the main value of the line
    #endmethod
    def finalPrint(self):
        #Define finalPrint() method
        print("----------------------------------------")
        print("            ITEMS PURCHASED             ")
        print("----------------------------------------")
        #First part of message
        self.nameAmnt()
        #Print name and amount of each individual item
        print("----------------------------------------")
        print("                 PRICE                  ")
        print("----------------------------------------")
        #Second part of message
        self.priceAmnt()
        #Print total of all items plus tax
        print("----------------------------------------")
        print("                PAYMENT                 ")
        print("----------------------------------------")
        #Third part of message
        self.debitAmnt()
        #Print payment method and change due
        print("----------------------------------------")
        print("         THANK YOU FOR SHOPPING         ")
        print("----------------------------------------")
        print("   ")
        print("   ")
        #Final part of message
    #endmethod
#endclass




