str = ("abcdefghijklmnopqrstuvwxyz")

# Slicing
slice = str[0:5:]

print(slice)

# Taking input from user 
start =int (input("Choose Starting Alpahet : "))
end =int (input("Choose End Alpabet : "))

slice = str[start:end:]

print(slice)


# Reverse Slicing
reverse = str[::-1]
print(reverse)

# Skip 
skip = str[0:9:3]
print(skip)

