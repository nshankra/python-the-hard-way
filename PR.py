from sys import argv

script, filename = argv

print(f"We're going to read {filename}.")
print("if you want that, hit CRTN-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file..............")
target =open(filename, 'w')

print("truncating the file. Goodbye!")
target.truncate()

line1 = input("")

print("I'm going to read these line for you")

target.read(line1)
target.read("\n")
target.read(line2)
target.read("\n")
target.read(line3)
target.read("\n")
target.close()
