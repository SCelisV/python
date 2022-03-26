def loadfile(filename):
    lines=[ ]
    file = open(filename,'rt')
    lines = file.readlines();
    file.close()
    return lines

def userinput(prompt):
   buffer = input(prompt)
   return buffer
