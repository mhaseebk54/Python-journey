fruit = ("apple","mango","banana","cherry","watermelon")
vegetable =("potato","tomato","onion","garlic","brinjal")
print(fruit)
# Length Check method

print (len(fruit))

# Type Check Method

print (type(fruit))

# Access Tuple

# Forward Access

print(fruit[1])

# Multi Access
print(fruit[0:2])

# Backward Access

print(fruit[-1])

# Multi Access
print(fruit[:4])

# Access till end

print(fruit[2:])


# Add To Tuples
add = fruit + vegetable
print(add)

# Nested Tuples print

tuple1 =("orange",(2,2,4),(4,6,2))
print(tuple1[1][2])


# Add in Tuples
num =(2,5,9,2,3,4,7)
total = sum(num)
print("total Sum : ",total)