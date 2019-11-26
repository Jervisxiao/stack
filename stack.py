class Stack():
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(items)-1]
    
    def size(self):
        return len(self.items)


    def parChecker(self,symbolString):
        balanced = True
        index = 0
        while index < len(symbolString) and balanced:
            symbol = symbolString[index]
            if symbol in "({[":
                self.push(symbol)
            elif symbol in ")}]":
                if self.is_Empty():
                    balanced = False
                else:
                    self.pop()

            index += 1
        if balanced and self.is_Empty():
            return True
        else:
            return False

    def printText(self,symbolString):
        if self.parChecker(symbolString) == True:
            index = 0
            text = ''
            while index < len(symbolString): 
                symbol = symbolString[index]
                if symbol in "(":
                    self.push(symbol)
                elif symbol in ")":
                    if self.is_Empty():
                        balanced = False
                    else:
                        self.pop()
                        if text != '':
                            print(str(self.size()) + ': ' + text)
                            text = ''                                              
                else:
                    text += symbolString[index]     
                index += 1


