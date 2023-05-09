# Reversing a string

string = "funny"
list = []
backwards = []
new_string = ""
num = 1

for i in string:
    list.append(i)

for i in range(len(list)):
    backwards.append(list[-num])
    num+=1

for i in backwards:
    new_string += i

print("")
print("Reversing a String (from Quora):")
print("")
print(f"Original string: {string}")
print(f"String reversed: {new_string}")

print("")
print("========================================")
print("========================================")
print("")

# Function for reversing string
def reverse_word(word):
    '''
        Provide a string and the function reverses it.
    '''
    string = word
    list = []
    backwards = []
    new_string = ""
    num = 1

    for i in string:
        list.append(i)

    for i in range(len(list)):
        backwards.append(list[-num])
        num+=1

    for i in backwards:
        new_string += i

    print("Inside a function:")
    print("")
    print(f"Original string: {string}")
    print(f"String reversed: {new_string}")
    print("")

# calling function
reverse_word("binky")




