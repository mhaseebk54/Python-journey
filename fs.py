# f = open("hello.txt")
# print(f.read())

file = open("hello.txt", "a+")

file.write("Adding a new line.")
file.seek(0)
print(file.read())
file.close()

file = open("hello.txt", "r")
lines = file.readlines()
print(lines)
file.close()

file = open("hello.txt", "r")
words = file.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
file.close()
