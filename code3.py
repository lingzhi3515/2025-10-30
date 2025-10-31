animals = ["cat", "dog", "rabbit", "elephant", "tiger"]
print("动物列表是:", animals)

print("第1个动物是:", animals[0])
print("倒数第3个动物是:", animals[-3])

animals.append("lion")
print("append添加后:", animals)

animals.insert(len(animals), "bear")
print("insert添加后:", animals)

animals[1] = "wolf"
print("修改第2个元素后:", animals)

del animals[3]
print("删除第4个元素后:", animals)

first_animal = animals.pop(0)
print(f"pop删除的元素: {first_animal}")
print("pop删除第一个元素后:", animals)

sorted_animals = sorted(animals)
print("sorted()排序结果:", sorted_animals)
print("原列表未被修改:", animals)

animals.sort()
print("sort()排序后原列表被修改:", animals)

reverse_sorted = sorted(animals, reverse=True)
print("sorted()倒排结果:", reverse_sorted)
print("原列表未修改:", animals)

animals.sort(reverse=True)
print("sort()倒排后原列表:", animals)

nums = list(range(2, 21, 2))
print("数字列表是:", nums)

squares_for = []
for num in nums:
    squares_for.append(num**2) 
print("for循环计算的平方：",squares_for)
squares_comprehension = [num ** 2 for num in nums]
print("列表推导式计算的平方:", squares_comprehension)

print(f"正数索引  {nums[5:10]}")
print(f"负数索引  {nums[-5:]}")

print("使用切片的拷贝")
nums2 = nums[:]
nums.append(777)
nums2.append(888)
print(f"第一个数组{nums}")
print(f"第二个数组{nums2}")
print("能起到拷贝后相互独立的效果")
print("不使用切片的拷贝")
nums3 = nums
nums.append(666)
nums3.append(999)
print(f"第一个数组{nums}")
print(f"第三个数组{nums3}")
print("不能起到拷贝后相互独立的效果")

str = ("I Love Python I Love Programing")
print("字符串为",str)

word_list = str.split()
print("分割为单词列表:")
print(f"{word_list}")

joined = ",".join(word_list)
print("单词列表用逗号连接:")
print(f"{joined}")

char_list = list(str)
print("分割为字符列表:")
print(f"{char_list}")

char_joined = "".join(char_list)
print("字符列表重新组合:")
print(f"{char_joined}")

nums = [0,2,1,0,4,0,0,3,0]
for i in range(0,7):
    for j in range(0,7-i):
        nums[j]
        nums[j+1]
        if nums[j]== 0:
            save = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = save
print("重新排列后的nums:",nums)

