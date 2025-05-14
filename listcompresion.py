list= [x**2 for x in range(1,11) ]
print (list)

nums = [23, 32, 21, 23, 45, 76]
a = [n for n in nums if n % 2 == 0]
print(a)

a = ["apple","mango","orange"]
upper= [n.upper() for n in a ]
print(upper)

lists = [[1, 2], [3, 4], [5, 6]]
ret = [item for sublist in lists for item in sublist]
print(ret)
