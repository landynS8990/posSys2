from fileHandler import handleFile

def write(nameOfFile):
    print('Creating new text file') 

    name = 'inventory.'+nameOfFile+'.txt'  # Name of text file coerced with +.txt

    file = open(name,'w+')   # Trying to create a new file or open one
    return file

a = write("date")