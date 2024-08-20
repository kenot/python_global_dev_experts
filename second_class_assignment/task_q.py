nums_list = [1, 2, -8, 0]

smallest_num = nums_list[0]

for num in nums_list:
    if num < smallest_num:
        smallest_num = num
print(smallest_num)
