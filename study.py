from pythonds.basic.stack import Stack
import re

#使用栈判断是否符合规则 ((())) 符合 (())))))不符合
# def count(s1,s2):
#     l1 =list(s1)
#     l2 = list(s2)
#     l1.sort()
#     l2.sort()
#     if l1 == l2:
#         return True
#     else:
#         return False
# c1 = count("abcd","baedc")
# print(c1)

# def perchecker(string):
#     s = Stack()
#     a = True
#     strnum = len(string)
#     index_num = 0
#     while index_num < strnum and a:
#         if string[index_num] == "(":
#             s.push(string[index_num])
#         else:
#             if s.isEmpty():
#                 a = False
#             else:
#                 s.pop()
#         index_num += 1
#     if a and s.isEmpty():
#         return True
#     else:
#         return False
#
# if __name__ == "__main__":
#      print(perchecker("(())))))"))
#      print(perchecker("((()))"))


# 使用栈，判断是否符合规则"){}{){)}" 不符合    ({[]}) 符合
# def perchecker2(string):
#     s = Stack()
#     res = True
#     num = len(string)
#     start = 0
#     while start < num and res != False:
#         if string[start] in "({[":
#             s.push(string[start])
#         else:
#             if s.isEmpty():
#                 res = False
#             else:
#                 top = s.pop()
#                 if not matche(top,string[start]):
#                     res = False
#         start += 1
#     if res != False and s.isEmpty():
#         return True
#     else:
#         return False
# def matche(open,close):
#     s1 = "({["
#     s2 = ")}]"
#     return s1.index(open) == s2.index(close)
#
#
# if __name__ == "__main__":
#     print(perchecker2("({[]})"))
#     print(perchecker2("){}{){)}"))


#十进制转二进制
# def per(num):
#     s = Stack()
#     while num > 0:
#         ten = num % 2
#         s.push(ten)
#         num = num // 2
#     string = ""
#     while not s.isEmpty():
#         string += str(s.pop())
#     return string
# if __name__ == "__main__":
#     print(per(233))

#计算表达式的转换
# (1+3) * 2     new = [(,1,3,),2] s = (,+,),*
def per(string):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    s = Stack()
    new = []
    tokenl = string.split()
    for token in tokenl:
        if re.match(r'[0-9A-Z]]',token):
            new.append(token)
        elif token == "(":
            s.push(token)
        elif token == ")":
            toptoken = s.pop()
            while toptoken != "(":
                new.append(toptoken)
                toptoken = s.pop()
        else:
            while (not s.isEmpty()) and \
            (prec[s.peek()] >= prec[token]):new.append(s.pop())
            s.push(token)

    while not s.isEmpty():
        new.append(s.pop())
    return "".join(new)








if __name__ == "__main__":
    per("(1+3)*2")






















