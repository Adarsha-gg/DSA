class stack:
    def __init__(self):
        self.__array = []

    def push(self,value):
        self.__array.append(value)

    def pop(self):
        if self.__array == []:
            raise IndexError
        self.__array.pop()

    def top(self):
        if self.__array == []:
            raise ValueError    
        return self.__array[-1]
        
    def size(self):
        return len(self.__array)


