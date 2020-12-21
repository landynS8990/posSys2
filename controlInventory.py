from __future__ import division
import itemStore as ItemStorage

from inputControl import classBecauseINeedToTurnTheseIntoMethodsForSomeReason
from fileHandler import handleFile


def similar(x,y):
    #Define similar() function to compare two lists
    si = 0
    #Define si as 0
    for a,b in zip(x, y):
        #Loop through a and b
        if a == b:
            #If the current index of a and b and equal
            si += 1
            #Add 1 to si
        #endif
    #endfor
    return (si/len(x)) * 100
    #Return their similarity as a percentage
#endfunction

inputClass = classBecauseINeedToTurnTheseIntoMethodsForSomeReason()
#Instantiate input class
handle = handleFile()
#Instantiate file handler class

class storeItem:
    #Define store item class
    def __init__(self, ids, name, category, quantity, minQuantity, vendPrice, sale):
        #Define __init__() method
        self.id = ids
        self.name = name
        self.category = category
        self.quantity = quantity
        self.minQuantity = minQuantity
        self.vendPrice = vendPrice
        self.sale = sale
        #Define store item variables
    #endmethod
    def retu(self):
        #Define retu() method to return an item from the shop formatted properly
        realPrice = (float(self.sale)/100.00) * self.vendPrice
        #Define realPrice as the vendor price multlied by the sale percentage as a decimal
        strMain = f"{self.id}, {self.name}, {self.category}, {self.quantity}, {self.minQuantity}, {self.vendPrice}, {self.sale}, {realPrice}"
        #Define strMain as all item variables as an fstring
        return strMain
        #Return strMain
    #endmethod
#endclass

class InventoryControl:
    #Define class inventoryControl
    def __init__(self, masterList):
        #Define __init__() method
        self.masterList = masterList
        #Define masterList as masterList argument(passed from main.py)
    #endmethod
    
    def inventoryMenu(self):
        #Define inventoryMenu method
        e = 0
        #Define e as 0
        while e < 1:
            #While e is less than 1
            Input = inputClass.createMenu("Your options are: ", "Item list", "Add item", "Add stock", "Delete item", "Modify item", "Search an item", "Exit", "Print items by category", "Print items under a certain quantity")
            #Create menu for selecting options
            if Input == "1":
                #If user selects 1
                ItemOutput(self.masterList).getAllItems()
                #Call to getAllItems() method from ItemOutput class in order to print all items in the catalogue
            elif Input == "7":
                #If user selects 7
                e += 1
                #Break loop
            elif Input == "3":
                #if user selects 3
                self.masterList = ItemModification(self.masterList).addStock()
                #Call to addStock() method from ItemModification class in order to add stock of a specific item
            elif Input == "2":
                #If User selects 2
                self.masterList = NewItem(self.masterList).getNewItem()
                #Call to getNewItem() method from newItem class in order to create a new item
            elif Input == "4":
                #If user selects 4
                self.masterList = ItemModification(self.masterList).deleteItem()
                #Call to deleteItem() method from ItemModification class in order to remove item from catalogue
            elif Input == "5":
                #If user selects 5
                self.masterList = ItemModification(self.masterList).changeData()
                #Call to changeData() method from ItemModification class in order to change details of a specific item
            elif Input == "6":
                #If user selects 6
                ItemOutput(self.masterList).searchForItem()
                #Call to searchForItem() method from ItemOutput class in order to print
            elif Input == "8":
                #If user selects 8
                ItemOutput(self.masterList).getAllCatItems(input("What category would you like to see: "))
            elif Input == "9":
                #If user selects 9
                ItemOutput(self.masterList).getAllCatItems(inputClass.getIntOnly("Display all items under what quantity: "))
            #endif
        #endwhile
        return self.masterList
        #Return masterList to main.py
    #endmethod
#endclass

class ItemOutput:
    #Define ItemOutput class
    def __init__(self, masterList):
        #Define __init__() method
        self.masterList = masterList
        #Define masterList as masterList argument
    #endmethod

    inputClass = classBecauseINeedToTurnTheseIntoMethodsForSomeReason()
    #Instantiate input control class
    def getAllItems(self):
        #Define getAllItems() method
        for i in self.masterList.inventory:
            #Loop through masterList inventory
            print(i)
            #Print current index
        #endfor
    #endmethod

    def getAllCatItems(self, cats):
        l = 0
        for i in self.masterList.inventory:
            cat = i[2].split("-")[1]
            if cats.lower() == cat.lower():
                l += 1
                print(i)
        if l == 0:
            print("Your query returned 0 results. Please ensure the category you want to search is typed correctly")
    def getAllQuantItems(self, cats):
        l = 0
        for i in self.masterList.inventory:
            cat = int(i[3])
            if int(cats) > cat:
                l += 1
                print(i)
        if l == 0:
            print("Your query returned 0 results. Please ensure the category you want to search is typed correctly")
    def searchForItem(self):
        #Define searchForItem() method
        e = inputClass.createMenu("How would you like to search?", "By product", "By item name")
        #Create user input menu
        if e == "1":
            #If user selects 1
            l = 0
            #Define l as 0
            searchQuery = input("Please Enter the SKU Number:     ")
            #Get user search query
            for t in self.masterList.inventory:
                #Loop through inventory
                print(t[0])
                #Print current SKU
                if searchQuery.lower() in t[0].lower():
                    #if search query matches product SKY
                    l += 1
                    #Add 1 to l
                    print("Your query returned:   ")
                    print(t)
                    #Print search result
                #endif
            #enfor
            if l == 0:
                #If l is 0(no results found)
                print("Your query returned 0 results")
                #Print message to user
            #endif
        elif e == "2":
            #If user selects 2
            searchQuery = input("Please Enter the item Name:     ")
            #Get user search query
            f = 0
            #Define f as 0
            otherList = []
            #Get list for list of results
            queryList = []
            #Define queryList as empty list
            for i in searchQuery:
                #Loop through searchQuery
                queryList += [i]
                #Append current index to list
            #endfor
            for t in self.masterList.inventory:
                #Loop through inventory
                resultList = []
                #Define resultList as 0
                for y in t[1]:
                    #Loop through current index
                    resultList += [y]
                    #Add current character to resultList
                print("   ")
                print(resultList)
                #Print the list of result characters
                print(queryList)
                #print the list of query characters
                print("   ")
                result = similar(queryList,resultList)
                #Compare how similar the two lists are
                if result > 50.0:
                    #if they're more than 60% alike
                    f += 1
                    #Add 1 to f
                    otherList += [t]
                    #Append current search result to otherList
                #endif
            print(f"Your query returned {f} results:   ")
            #Print message to user
            print("   ")
            for b in otherList:
                #Loop through otherList
                print(b)
                #Print current index
            #endfor
        else:
            #If user selects 3
            print("Exiting...")
            #Print message
        #endif
    #endmethod
#endclass

class ItemModification:
    #Define class ItemModification
    def __init__(self, masterList):
        #Define __init__() method with masterList argument
        self.masterList = masterList
        #Define masterList as masterList argument
    #endmethod

    inputClass = classBecauseINeedToTurnTheseIntoMethodsForSomeReason()
    #Instantiate input control class

    def addStock(self):
        #Define add stock method
        l = 0
        #Define l as 0
        e = inputClass.createMenu("How would you like to add stock?", "By item", "By category", "Exit")
        #Create selection menu for user
        if e == "1":
            #If user selects 1
            q = 0
            l = 0
            #Define q and l as 0
            searchQuery = input("Please Enter the product ID:     ")
            #Get user search query
            for t in self.masterList.inventory:
                #Loop through inventory
                print(t[0])
                #Print current index SKU
                if searchQuery.lower() in t[0].lower():
                    #If current index SKU matches search query
                    l += 1
                    #Add 1 to l
                    print("Current product details:   ")
                    print(t)
                    #Print product details
                    y = inputClass.getIntOnly("How much more stock would you like to add?")
                    #Get added stock as integer
                    tot = self.masterList.inventory[q][3] + y
                    self.masterList.inventory[q][3] = tot
                    #Add user inputted quantity to self.masterList.inventory
                    newStr = ""
                    #Define newStr as empty string
                    for n in self.masterList.inventory[q]:
                        #Loop through current index
                        newStr += f"{n} "
                        #Add current item to newStr string with spacing
                    #endfor
                    newStr += '\n'
                    #Add line break to newStr
                    print("   ")
                    print(newStr)
                    print("   ")
                    #Print new product listing in inventory.txt
                    handle.replace_line(self.masterList.inventory[q][0], newStr)
                    #Replace current listing with updated one
                #endif
                q += 1
                #Add 1 to q
            if l == 0:
                #If l is 0(No matching items were found)
                print("Item not found. Please ensure query is accurate")
                #Print message to user
        elif e == "2":
            q = 0
            #Define q as 0
            searchQuery = input("Please Enter the item Name:     ")
            #Get user search query
            f = 0
            #Define f as 0
            for t in self.masterList.inventory:
                #Loop through inventory
                if t[1].lower() == searchQuery.lower():
                    #If search query matches current index product name
                    l += 1
                    #Add 1 to l
                    print("Current product details:   ")
                    print(t)
                    #Print product details
                    y = inputClass.getIntOnly("How much more stock would you like to add?")
                    #Get added stock as integer
                    tot = self.masterList.inventory[q][3] + y
                    self.masterList.inventory[q][3] = tot
                    #Update inventory with new stock
                    newStr = ""
                    #Define newStr as empty string
                    for n in self.masterList.inventory[q]:
                        #Loop through current index
                        newStr += f"{n} "
                        #Add current item to newStr string with spacing
                    #endfor
                    newStr += '\n'
                    #Add line break to newStr
                    print("   ")
                    print(newStr)
                    print("   ")
                    #Print new product listing in inventory.txt
                    handle.replace_line(self.masterList.inventory[q][0], newStr)
                    #Replace current listing with updated one
                #endif
                q += 1
                #Add 1 to q
            if l == 0:
                #If l is 0(No matching items were found)
                print("Item not found. Please ensure query is accurate")
                #Print message to user

        else:
            #If user selects 3
            return self.masterList.inventory
            #Return inventory
        #endif
        return self.masterList
        #Return masterList
    #endmethod
    
    def deleteItem(self):
        #Define deleteItem() method
        l = 0
        #Define l as 0
        e = inputClass.createMenu("Which product would you like to modify?", "Search by ID", "Search by name")
        #Create user input menu
        if e == "1":
            #If user selects 1
            q = 0
            #Define q as 0
            l = 0
            #Define l as 0
            searchQuery = input("Please Enter the product ID:     ")
            #Get user search query
            for t in self.masterList.inventory:
                #Loop through inventory
                print(t[0])
                #Print current index SKU
                if searchQuery in t[0]:
                    l += 1
                    #If search query is equal to current index  SKU
                    confirm = inputClass.createMenu(f"Are you sure you want to delete {t[1]} from the shop's catalogue?", "Yes", "No")
                    #Get confirmation menu
                    if confirm == "1":
                        #If user selects 1(Yes)
                        del self.masterList.inventory[q]
                        #Remove item from inventory
                        handle.delete_line(searchQuery)
                        #Delete line in inventory.txt
                        print("Item has been deleted")
                        #Print message to user
                    else:
                        #If user selects 2(No)
                        print("   ")
                        print("Exiting...")
                        print("   ")
                        #Print message to user
                    #endif
                #endif
                q += 1
                #Add 1 to q
            #endfor
            if l == 0:
                #If l is still 0(No matching items were found)
                print("Item not found. Please ensure query is accurate")
                #Print message to user
            #endif
        elif e == "2":
            #If user selects 2
            q = 0
            #Define q as 0
            searchQuery = input("Please Enter the item Name:     ")
            #Get search query from user
            f = 0
            #Define f as 0
            for t in self.masterList.inventory:
                #Loop through inventory
                if t[1] == searchQuery:
                    #If search query is equal to current index name
                    confirm = inputClass.createMenu(f"Are you sure you want to delete {t[1]} from the shop's catalogue?", "Yes", "No")
                    #Get confirmation menu
                    if confirm == "1":
                        #If user selects 1(Yes)
                        del self.masterList.inventory[q]
                        #Remove item from inventory
                        handle.delete_line(searchQuery)
                        #Delete line in inventory.txt
                        print("Item has been deleted")
                        #Print message to user
                    else:
                        #If user selects 2(No)
                        print("   ")
                        print("Exiting...")
                        print("   ")
                        #Print message to user
                    #endif
                #endif
                q += 1
                #Add 1 to q
            #endfor
            if l == 0:
                #If l is still 0(No matching items were found)
                print("Item not found. Please ensure query is accurate")
                #Print message to user
            #endif
        else:
            #If otherwise
            return
            #Return nothing
        #endif
        return self.masterList
        #Return masterList
    #endmethod

    def changeData(self):
        #Define changeData() method
        e = inputClass.createMenu("Which product would you like to modify?", "Search by ID", "Search by name")
        #Create user selection menu
        l = 0
        #Define l as 0
        if e == "1":
            #If user selects 1
            q = 0
            #Define q as 0
            searchQuery = input("Please Enter the product ID:     ")
            #Get user search query
            for t in self.masterList.inventory:
                #Loop through inventory
                print(t[0])
                #Print current index SKU
                if searchQuery.lower() in t[0].lower():
                    #If searchQuery matches current index SKU
                    l += 1
                    #Add 1 to l
                    print("Current product details:   ")
                    print(t)
                    #Print current product details
                    i = 0
                    #Define i as 0
                    while i < 1:
                        #While i is less than 1
                        u = inputClass.createMenu("What would you like to do?", "Modify product name", "Modify type", "Modify minimum quantity", "Modify vendor price", "Put item on sale", "Exit")
                        #Create menu for user
                        if u == "1":
                            #If user selects 1
                            nm = input("What's the new product name? ")
                            #Get user string input
                            self.masterList.inventory[q][1] = nm
                            #Replace current index name with user input
                        elif u == "2":
                            #If user selects 2
                            enumVal = inputClass.createMenu('Select a Category For This Item:   ', 'OTHER', 'MEAT', 'FRUIT', 'VEGETABLE')
                            #Get user menu category input
                            typ = ItemStorage.ItemCategory(int(self.newItemEnumValue) - 1)
                            #Convert to enum
                            self.masterList.inventory[q][2] = typ
                            #Replace current index category with user input
                        elif u == "3":
                            #If user selects 3
                            quan = inputClass.getIntOnly("New minimum quantity:   ")
                            #Get new minimum quantity as int from user
                            self.masterList.inventory[q][4] = quan
                            #Replace current index minimum quantity with quantity
                        elif u == "4":
                            #If user selects 4
                            vend = inputClass.getFloatOnly("New price:   ")
                            #Get new vendor price as float from user
                            self.masterList.inventory[q][7] = str(float(r) * float(self.masterList.inventory[q][6]))
                            #Replace current index vendor price with user input
                        elif u == "5":
                            #If user selects 5
                            sal = inputClass.getFloatOnly("New sale %:   ")
                            #Get new sale as percentage
                            k = sal / 100.00
                            #Divide by 100 to get as decimal
                            print(k)
                            #Print decimal sale
                            print(self.masterList.inventory[q][5])
                            #Print current vendor price
                            r = float(k) * (float(self.masterList.inventory[q][7]) / float(self.masterList.inventory[q][6]))
                            #Multiply by current price to get updated price with new sale
                            self.masterList.inventory[q][7] = r
                            #Set new price
                            self.masterList.inventory[q][6] = k
                            #Set new sale value
                        elif u == "6":
                            #if user selects 6
                            i += 1
                            #Break loop
                        #endif
                    #endwhile

                    newStr = ""
                    #Define newStr as empty string
                    for n in self.masterList.inventory[q]:
                        #Loop through current index
                        newStr += f"{n} "
                        #Add current item to newStr string with spacing
                    #endfor
                    newStr += '\n'
                    #Add line break to newStr
                    print("   ")
                    print(newStr)
                    print("   ")
                    #Print new product listing in inventory.txt
                    handle.replace_line(self.masterList.inventory[q][0], newStr)
                    #Replace current listing with updated one
                #endif
                q += 1
                #Add 1 to q
            #endfor
            if l == 0:
                #If l is still 0(No matching items were found)
                print("Item not found. Please ensure query is accurate")
                #Print message to user
        elif e == "2":
            #If user selects 2
            q = 0
            #Define q as 0
            searchQuery = input("Please Enter the item Name:     ")
            #get user search query
            f = 0
            #Define f as 0
            for t in self.masterList.inventory:
                #Loop through inventory
                if t[1] == searchQuery:
                    #if searchQuery is equal to current index name

                    l += 1
                    #Add 1 to l
                    print("Current product details:   ")
                    print(t)
                    #Print current product details
                    i = 0
                    #Define i as 0
                    while i < 1:
                        #While i is less than 1
                        u = inputClass.createMenu("What would you like to do?", "Modify product name", "Modify type", "Modify minimum quantity", "Modify vendor price", "Put item on sale", "Exit")
                        #Create menu for user
                        if u == "1":
                            #If user selects 1
                            nm = input("What's the new product name? ")
                            #Get user string input
                            self.masterList.inventory[q][1] = nm
                            #Replace current index name with user input
                        elif u == "2":
                            #If user selects 2
                            enumVal = inputClass.createMenu('Select a Category For This Item:   ', 'OTHER', 'MEAT', 'FRUIT', 'VEGETABLE')
                            #Get user menu category input
                            typ = ItemStorage.ItemCategory(int(self.newItemEnumValue) - 1)
                            #Convert to enum
                            self.masterList.inventory[q][2] = typ
                            #Replace current index category with user input
                        elif u == "3":
                            #If user selects 3
                            quan = inputClass.getIntOnly("New minimum quantity:   ")
                            #Get new minimum quantity as int from user
                            self.masterList.inventory[q][4] = quan
                            #Replace current index minimum quantity with quantity
                        elif u == "4":
                            #If user selects 4
                            vend = inputClass.getFloatOnly("New vendor price:   ")
                            #Get new vendor price as float from user
                            self.masterList.inventory[q][5] = r
                            #Replace current index vendor price with user input
                        elif u == "5":
                            #If user selects 5
                            sal = inputClass.getFloatOnly("New sale %:   ")
                            #Get new sale as percentage
                            k = sal / 100.00
                            #Divide by 100 to get as decimal
                            print(k)
                            #Print decimal sale
                            print(self.masterList.inventory[q][5])
                            #Print current vendor price
                            r = float(k) * (float(self.masterList.inventory[q][7]) / float(self.masterList.inventory[q][7]))
                            #Multiply by current price to get updated price with new sale
                            self.masterList.inventory[q][7] = r
                            #Set new price
                            self.masterList.inventory[q][6] = k
                            #Set new sale value
                        elif u == "6":
                            #if user selects 6
                            i += 1
                            #Break loop
                        #endif
                    #endwhile

                    newStr = ""
                    #Define newStr as empty string
                    for n in self.masterList.inventory[q]:
                        #Loop through current index
                        newStr += f"{n} "
                        #Add current item to newStr string with spacing
                    #endfor
                    newStr += '\n'
                    #Add line break to newStr
                    print("   ")
                    print(newStr)
                    print("   ")
                    #Print new product listing in inventory.txt
                    handle.replace_line(self.masterList.inventory[q][0], newStr)
                    #Replace current listing with updated one
                #endif
                q += 1
                #Add 1 to q
            if l == 0:
                #If l is still 0(No matching items were found)
                print("Item not found. Please ensure query is accurate")
                #Print message to user
        else:
            #if user inputs 3
            return
            #Return nothing
        #endif
        return self.masterList
        #Return masterList
    #endmethod
#endclass
class NewItem:
    #Define NewItem class
    def __init__(self, masterList):
        #Define __init__() method
        self.masterList = masterList
        #Define masterList as masterList
    #endmethod

    inputClass = classBecauseINeedToTurnTheseIntoMethodsForSomeReason()
    #Instantiate input control class
    def getNewItem(self):
        #Define getNewItem function to create new item and add it to the shop's inventory
        self.newName = input('Item name:  ')
        print("   ")
        #Get item name
        self.newItemEnumValue = inputClass.createMenu('Select a Category For This Item:   ', 'OTHER', 'MEAT', 'FRUIT', 'VEGETABLE')
        print("   ")
        #get item category
        self.newItemType = ItemStorage.ItemCategory(int(self.newItemEnumValue) - 1)
        print("   ")
        #Convert item category
        self.newQuantity = inputClass.getIntOnly('Enter the Quantity For This Item:   ')
        print('   ')
        #Get item quantity
        self.newMinQuantity = inputClass.getIntOnly('Enter the Minimum Quantity For This Item:   ')
        print("   ")
        #Get Item minimum quantity
        self.newVendorPrice = inputClass.getFloatOnly('Enter the Vendor Price For This Item:   ')
        print("   ")
        #Get item vendor price
        self.newSale = inputClass.getFloatOnly('Enter the Sale For This Item (%):   ')
        print("   ")
        #Get sale percentage
        self.createNewItem()
        #Create new item
        return self.masterList
        #Return masterList
    #endmethod

    def createNewItem(self):
        #Define createNewItem() method
        e = storeItem(self.newSku(self.newItemType), self.newName, self.newItemType, self.newQuantity, self.newMinQuantity, self.newVendorPrice, self.newSale).retu()
        #Call storeItem() method to return all data in storable fashion
        mainList = e.split(", ")
        #Split item string into list
        handleFile.addLine(mainList)
        #Add list to inventory.txt
        self.masterList.inventory.append(mainList)
        #Append new list to inventory list
        return self.masterList
        #Return master list
    #endmethod

    def newSku(self, cats):
        #Define newSku function to create new item SKU
        t = 0
        #Define t as 0
        h = 0
        #Define h as 0
        cat = (str(cats).split("."))[1]
        #Get category from input
        try:
            fort = 1
            #Define fort as 1
            g = ""
            #Define g as empty string
            catList = []
            #Define catList as empty list
            for k in self.masterList.inventory:
                #Loop through inventory
                print(k)
                #Print current index
                if str(cats) == str(k[2]):
                    #If the current index is of the same category as the item we're trying to create
                    fort += 1
                    #Add 1 to fort to get how many other items of the same category there are
                    catList += [k]
                    #Append current index to catList to get a list of items of the same category
            if fort < 2:
                #If fort is less than 2(If there are no other items of the same category in the inventory)
                h = f"{cat}-0001"
                #Create first SKU of the category
            else:
                #If not
                mul = 4 - len(str(fort))
                zeros = "0" * mul
                #Get number of zeros needed to make the latter half of the SKU exactly 4 characters
                h = f"{cat}-{zeros}{str(fort)}"
                #Create SKU with fstring
            #endif
        except:
            #If something goes wrong(nothing in inventory)
            print("No existing items")
            #Print message to user
            h = f"{cat}-0001"
            #Create first item in catalogue
        #endexcept
        return h
        #Return SKU
    #endmethod
#endclass


