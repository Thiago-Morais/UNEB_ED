file = open("soy akivu.txt")
lines = file.readlines()
print(lines)
file.writelines(lines)
file.close()
