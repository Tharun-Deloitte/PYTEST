class StringClass:
    def __init__(self,demo):
        self.demo=demo
    def list(self):
        return(list(self.demo))
    def length(self):
        return len(self.demo)


n=input("Enter a string :")
object1=StringClass(n)
print(object1.list())
print(object1.length())
