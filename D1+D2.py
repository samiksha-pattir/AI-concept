from collections import Counter
import re

# ---------------------------------------------------
# TOPIC: List comprehension
# builds a new list in one line: [expr for item in iterable if condition]
# ---------------------------------------------------
# odd= [1,2,3,4,5,6,7,8,9,10]
# # # odd = [10, 20, 30, 40, 50,21]
# # # sqr = [x**2 for x in odd if x%2!=0]   # loop over VALUES (x), not index
# # # print(sqr)

# ---------------------------------------------------
# TOPIC: Generator expression
# same syntax as list comprehension but with () instead of []
# does NOT build the whole list in memory - gives one value at a time
# ---------------------------------------------------
# sqr = (x**2 for x in odd if x%2!=0)

# # # print(next(sqr))   # each next() call computes ONE value, then pauses
# # # print(next(sqr))
# # # print(next(sqr))
# for i in sqr:
#     print(i)



# 0,1,1,2,3,5
# ---------------------------------------------------
# TOPIC: yield / generator function
# yield pauses the function and returns a value, next() resumes from there
# used when data is too big to store all at once (memory efficient)
# ---------------------------------------------------
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


# ---------------------------------------------------
# TOPIC: File handling with 'with'
# 'with' auto-closes the file even if an error happens inside the block
# ---------------------------------------------------
# def fl(fileName):
#     with open(fileName) as file:
#         k=file.read()
#         k=k.lower()
#         return k



# print(fl("file.txt"))


# ---------------------------------------------------
# TOPIC: re.findall + Counter + try/except
# re.findall(r"\w+", text) pulls out words, ignoring punctuation
# Counter counts how many times each word appears
# try/except here wraps the FUNCTION CALL (not the definition) so a missing
# file doesn't crash the whole script
# ---------------------------------------------------
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
#     print(f"file {e.filename} is not there")   # e.filename = built-in attr on the error


# ---------------------------------------------------
# TOPIC: Custom exception
# class InheritName(Exception): pass -> makes a new error type
# used when built-in errors (ValueError, etc) don't describe the exact problem
# ---------------------------------------------------
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


# ---------------------------------------------------
# TOPIC: Context manager (__enter__ / __exit__)
# these are FIXED method names Python looks for when you use 'with'
# __enter__ runs at the start of the with-block, __exit__ runs at the end
# (even if an error happens) - return self so 'as r' gives you the object
# ---------------------------------------------------
# class Run:
#     def __enter__(self,):
#         print("hello this is starting ")
#         return self
#     def __exit__(self, e, f, g):
#         print("this is the end ")


# with Run() as r:
#     print("work is done")


# =====================================================
# DAY 2 MINI PROJECT: CSVCleaner
# combines: custom exception + context manager + try/except INSIDE a loop
# so one bad (empty) row is skipped without stopping the whole file read
# =====================================================

class RunBadRow(Exception):
    pass

class CSVCleaner:
    def __init__(self, fileName):
        self.fileName = fileName   # just store the filename, don't open yet

    def __enter__(self):
        self.file = open(self.fileName)  # self. so other methods can use it too
        return self                       # so 'as c' gives the whole object, not None

    def __exit__(self, exc_type, exc, tb):
        self.file.close()   # guaranteed cleanup when the with-block ends

    def clean(self):
        goodCount = 0
        badCount = 0
        data = []
        for line in self.file:              # loop over the FILE OBJECT, not the filename string
            line = line.strip()             # remove newline/extra spaces
            try:
                if line == "":
                    raise RunBadRow("there is an empty row ")

                goodCount += 1
                data.append(line)
            except RunBadRow as e:
                # try/except is INSIDE the loop -> only this row is skipped,
                # the loop keeps going for the rest of the rows
                print(f"skip this : {e}")
                badCount += 1
        print(f"total good count = {goodCount} \n total bad count = {badCount}")
        return data


with CSVCleaner("kk.txt") as c:
    r = c.clean()
    print(r)
