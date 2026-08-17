import numpy as np
import time as t
# # import pprint as p

# # p.pprint(dir(np))

# # ---------------------------------------------------
# # TOPIC: NumPy array vs Python list
# # a numpy array stores same-type data together in memory -> fast math ops
# # math operators (+, *, >) apply to EVERY element at once (vectorization)
# # ---------------------------------------------------
# data=np.array([10,20,30,40])
# # print(data+20)              # adds 20 to every element

# # # print(max(data)+80)
# # # print(data*2)              # multiplies every element by 2


# # ---------------------------------------------------
# # TOPIC: Boolean indexing (filtering without a loop)
# # data > 20 makes a True/False array, data[mask] keeps only the True ones
# # ---------------------------------------------------
# # result=data[data>20]
# # print(result)


# # data = np.array([5, 12, 8, 25, 3, 40])
# # res=data[data>10]        # only values greater than 10
# # print(res)

# # 2D Array like a table

# # dimensions — (rows, columns).

# # ---------------------------------------------------
# # TOPIC: 2D array (matrix) - shape, row access, column access
# # shape = (rows, columns)
# # arr[i]      -> whole row i
# # arr[:, j]   -> whole column j  (':' means "take all rows")
# # ---------------------------------------------------
# students_data=np.array([
#     [20,40,30,90],
#     [50,20,60,33],
#     [500,2000,600,303]
# ])
# # print(students_data[0][2])   # row 0, column 2

# # print(np.shape(students_data))
# # (2, 4)
# # ("rows", "columns")
# # print(students_data[0])          # whole row 0
# # print(students_data[1])          # whole row 1
# # print(students_data[:, 2])    # pura column 1


# # ---------------------------------------------------
# # TOPIC: Broadcasting
# # n has shape (3,), m has shape (2,3) -> numpy "stretches" n to match
# # every row of m, so n gets added to BOTH rows without a loop
# # ---------------------------------------------------
# m = np.array([[1, 2, 3],
#               [4, 5, 6]])


# n=np.array([10,20,30])

# print(m+n)
# # print(np.dot(m))
# # print(m.T)                        # transpose - rows become columns
# # print(m.dot(m.T))
# # print(np.linalg.norm(m))          # "size" of all numbers combined
# # print(np.sum(m, axis=0))          # axis=0 -> sum going DOWN (column-wise result)
# # print(np.sum(m, axis=1))          # axis=1 -> sum going ACROSS (row-wise result)
# #         ┌─────────────────────────┐
# #         │   10   20   30   90     │  ← row 0
# # axis=0  │                          │
# #   │     │   50   20   60   33     │  ← row 1
# #   ▼     └─────────────────────────┘
# #      (rows ke across,
# #       TOP-BOTTOM)


# # ---------------------------------------------------
# # TOPIC: Dot product + Transpose + Norm
# # np.dot(a, b): a's columns must match b's rows -> each result cell =
# # (a's row) matched element-by-element with (b's column), then summed
# # a.T: flips rows and columns
# # np.linalg.norm(a): squares every element, adds them, takes square root
# # -> one number showing the overall "size" of the array
# # ---------------------------------------------------
# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
#     ])
# b = np.array([
#     [1, 0],
#     [0, 1],
#     [1, 1]
# ])
# print(np.dot(a,b))
# print(a.T)

# print(np.linalg.norm(a))

def slow_square_sum(arr):
    # ea=[]
    s=0
    for i in arr:
        k=i**2
        s+=k
    return s





def fast_square_sum(arr):
    rs=np.sum(arr**2)
    return rs

data=np.arange(1_000_000)


start=t.time()  
print(slow_square_sum(data))
en=t.time() 
print(en-start) 
x=en-start

start=t.time()  
print(fast_square_sum(data))
en=t.time() 
print(en-start) 
y=en-start
print(x>y)

