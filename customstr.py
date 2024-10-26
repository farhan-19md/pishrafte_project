class customstr:
    def __init__(self,str_test):
        self.str_test = str_test
    def remove_duplicate(self):
        test_lst = []
        for i in self.str_test:
            test_lst.append(i)
        a = ""
        for i in test_lst:
            if i not in a:
                a += i
        return a
    def set(self,index,word):
        test_lst = []
        res = ""
        for i in self.str_test:
            test_lst.append(i)
        for i in range(len(test_lst)):
            if i == index:
                test_lst[i] = word
        for i in test_lst:
            res += i
        return res
    def isfloat(self):
        self.str_test = float(self.str_test)
        if type(self.str_test) == float:
            return True
        else:
            return False
    def ispalindrome(self):
        test_lst = []
        for i in self.str_test:
            test_lst.append(i)
        for i in range(len(test_lst) // 2):
            if test_lst[i] == test_lst[len(test_lst) - 1 - i]:
                return True
            else:
                return False
            
x = customstr("python")
# print(x.isfloat())
# print(x.remove_duplicate())
# print(x.set(0,"n"))
print(x.ispalindrome())