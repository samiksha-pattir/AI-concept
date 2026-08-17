# import numpy as np
# # # Day 04 — NumPy Advanced: Indexing & Memory
# # # Concept 1: Fancy indexing

# # arr = np.array([10,20,30,40,50,60])
# # slice_arr=arr[2:5]
# # print(f"this is slice from arr {slice_arr}")
# # print(slice_arr[0])
# # slice_arr[0]=9999
# # # print(slice_arr)
# # print(arr)


# # # fancy index
# # f_arr=arr[[0,2,4]]
# # # f_arr[0]=777
# # # # print(f_arr)
# # # print(arr)


# # # Concept 3: reshape
# # arr = np.arange(12)
# # print(arr.shape)

# # # 2 rows 3 columns 

# # sh1=arr.reshape (3, 4)
# # print(sh1)



# # # # 3 rows 2 columns 
# # sh2=arr.reshape(2,-1)
# # print(sh2)


# def get_first_three(data):
#     return data[0:3].copy()    # view return kar raha

# sensor_data = np.array([100, 200, 300, 400, 500])
# sample = get_first_three(sensor_data)

# sample[0] = 0            # sirf "sample" ko badalna tha, testing ke liye

# print(sensor_data)        # BUG: original bhi badal gaya!





