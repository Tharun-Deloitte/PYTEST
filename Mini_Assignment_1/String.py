class StringClass:

    def __init__(self,string):
        self.string=string

    def list(self):
        return (list(self.string))

    def length(self):
        return len(self.string)

class PairsPossible(StringClass):

    def pair(self,test_list):
        result = [(n,j) for idx,n in enumerate(test_list)for j in test_list[idx+1:]]
        print(result)

class SearchCommonElements(StringClass):

    def common(self,str1,str2):
        str3 = list(set(str1) & set(str2))
        print(str3)



string1=input("Enter a string :")
object1=StringClass(string1)
print(object1.list())
print(object1.length())
list1=object1.list()

object2=PairsPossible(object1)
object2.pair(list1)

string2=input("Enter string to compare :")
object3=SearchCommonElements(list1)
object3.common(string1,string2)


