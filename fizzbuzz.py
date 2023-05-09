# SOLVED: FizzBuzz Challenge.
for i in range(101):
    if i == 0:
        continue
    if i%3 == 0 and i%5 == 0:
        print(f"{i} | FizzBuzz")
    elif i%3 == 0:
        print(f"{i} | Fizz")
    elif i%5 == 0:
        print(f"{i} | Buzz")
    else:
        print(i)

print("==========================")

def fizzbuzz(range_num, first_num, second_num):
    for i in range(range_num):
        if i == 0:
            continue
        if i % first_num == 0 and i % second_num == 0:
            print(f"{i} | FizzBuzz")
        elif i % first_num == 0:
            print(f"{i} | Fizz")
        elif i % second_num == 0:
            print(f"{i} | Buzz")
        else:
            print(i)
            
fizzbuzz(200, 5, 8)