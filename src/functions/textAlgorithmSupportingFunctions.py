
def createArray(text):
    textListOne = [text]
    textList = ([i for item in textListOne for i in item.split()]) 
    return textList

def parseInt(string):
    rString = ""
    for element in range(0, len(string)): 
        if RepresentsInt(string[element]):
            rString = rString + string[element]
    return rString

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

