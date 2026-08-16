from collections import Counter
import re
# odd= [1,2,3,4,5,6,7,8,9,10]
# # # odd = [10, 20, 30, 40, 50,21]
# # # sqr = [x**2 for x in odd if x%2!=0]
# # # print(sqr)

# sqr = (x**2 for x in odd if x%2!=0)

# # # print(next(sqr))
# # # print(next(sqr))
# # # print(next(sqr))
# for i in sqr:
#     print(i)



# 0,1,1,2,3,5
# def feb(n):
#     a,b=0,1
#     c=0
#     while c<n:
#         yield a  #0
#         a,b=b,a+b
#         # a= 1 and b= 0+1
#         c+=1

# for i in feb(10):
#     print(i, end=" ")
#     # one time one value 

    
# def fl(fileName):
#     with open(fileName) as file:
#         k=file.read()
#         k=k.lower()
#         return k



# print(fl("file.txt"))


   
# def fl(fileName):
#     with open(fileName) as file:
#         k=file.read().lower()
#         k=re.findall(r"\w+", k)
#         return k

# try:
#     res=fl("file.txt")
#     c=Counter(res)
#     print(c.most_common(10))
# except FileNotFoundError as e:
#     print(f"file {e.filename} is not there")

# class IncorrectData(Exception):
#     pass


# def cp(price):
#     if price<0:
#         raise IncorrectData(f" {price} is incorrect price value ")
#     return price


# try:
#     k= cp(100)
#     print(k)
    
# except IncorrectData as e :
#     print(f"Data issues {e}")




# class Run:
#     def __enter__(self,):
#         print("hello this is starting ")
#         return self
#     def __exit__(self, e, f, g):
#         print("this is the end ")


# with Run() as r:
#     print("work is done")

class CSVCleaner:
    def __init__(self, fileName):
        self.fileName=fileName

    def __enter__(self):
        self.file=open(self.fileName)
        return self
    def __exit__(self, exc_type, exc, tb):
        self.file.close()



with CSVCleaner("kk.txt") as c:
    print(c.file)


