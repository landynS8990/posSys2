
class classBecauseINeedToTurnTheseIntoMethodsForSomeReason:
    #Defibe the input class
    def checkFloat(self, inu):
        floatList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        #Define a list of string floats to compare the input to
        t = ""
        #Define blank string
        r = 0
        ##Index number
        for l in inu:
            #Loop through input string
            print(l)
            #Print current string index
            if l in floatList:
                #If the current index is in the list of possible values within a float
                t += l
                #If it is, add it to the string
            else:
                #If not
                r += 1
                #Add 1 to r
            #endif
        #endfor
        if r == 0:
            #If r is 0(no non-float characters were found)
            if "." not in t:
                #if there isn't a decimal(number is perfectly even)
                t += ".00"
                #Add .00 to the string to turn it into a float
            return t
            #Return the updated string
        else:
            #If some non-float characters were found
            return False
            #Return false
        #endif
    #endmethod
    def checkInt(self, inu):
        #Get only integer input
        intList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        #Define a list of string integers to compare the input to
        t = ""
        #Define blank string
        r = 0
        #Index number
        for l in inu:
            #Loop through input string
            print(l)
            #Print current index
            if l in intList:
                #If the current index is in the list of possible values within an int
                t += l
                #If it is, add it to the string
            else:
                #If not
                r += 1
                #Add 1 to r
            #endif
        #endfor
        if r == 0:
            #If r is 0(no non-int characters were found)
            return t
            #Return the string
        else:
            #If some non-int characters were found
            return False
            #Return false
        #endif
    #endmethod
    def getFloatOnly(self, strMsg):
        #Function to ensure user types float
        u = 0
        #Define u as 0
        while u < 1:
            #While u is under 1
            inu = input(strMsg)
            #Get user input with message
            t = self.checkFloat(inu)
            #Run user input through checkfloat
            if t != False:
                #If t isn't false(a float was inputted)
                u += 1
                #Break loop
                return float(t)
                #Return float of t
            else:
                #If not
                print("Please enter a float")
                #Keep running loop, ask user to enter float
            #endif
        #endwhile
    #endmethod
    def getIntOnly(self, strMsg):
        #Function to make sure user types int
        u = 0
        #Define u as 0
        while u < 1:
            #While u is less than 1
            inu = input(strMsg)
            #Get user input with message
            t = self.checkInt(inu)
            #Check if input is integer
            if t != False:
                #If t isn't false(an int was inputted)
                u += 1
                #Break loop
                return int(t)
                #Return integer of t
            else:
                #If not
                print("Please enter only integers")
                #Keep running loop with message
            #endif
        #endwhile
    #endmethod
    def createMenu(self, msg, *argv):
        #Function to create user selection menu
        numbList = []  
        #Define list of option numbers
        print("   ")
        print(msg)
        print("   ")
        #Print message to user
        e = 0
        #Define e as 0
        for i in argv:
            #Loop through option arguments
            e += 1
            #Add 1 to e
            print(f"{e}. {i}")
            #Print option number + option
            numbList += [str(e)]
            #Append e to list of accepted inputs
        #endfor
        t = 0
        #Define t as 0
        print(numbList)
        #Print list of accepted options
        while t < 1:
            #While t is less than 1
            r = input("Enter your selection: ")
            #Get user input
            if r in numbList:
                #If user entered one of the accepted options
                t += 1
                #break loop
                return r
                #Return option number selected
            else:
                #If not
                print("Invalid input. Please enter one of the selections above")
                #Keep running loop + print message to user
            #endif
        #endwhile
    #endmethod
#endclass

