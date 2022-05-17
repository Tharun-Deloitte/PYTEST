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

class EqualSumPairs():

    def pair(self,test_list):
        uniqueSums=[]
        result = [sum((int(n),int(j))) for idx,n in enumerate(test_list) for j in test_list[idx+1:]]
        print(result)
        n=len(result)
        sums = dict()
        for num in range(n):
            if result[num] in sums.keys():
                sums[result[num]] += 1
            else:
                sums[result[num]] = 1
        for num in sums:
            if sums[num] == 1:
                uniqueSums.append(num)
        print(uniqueSums)
        print(len(uniqueSums))


string1=input("Enter a string :")
object1=StringClass(string1)
print(object1.list())
print(object1.length())
list1=object1.list()

pairs=PairsPossible(object1)
pairs.pair(list1)

string2=input("Enter string to compare :")
compare=SearchCommonElements(list1)
compare.common(string1,string2)

print('sum of pairs')
uniquesum=EqualSumPairs()
uniquesum.pair(list1)