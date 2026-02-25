filename = input("Enter filename to open: ")
with open(filename, 'r') as file:
    data = file.read()
print(data)