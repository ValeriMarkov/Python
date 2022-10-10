import sympy  # imported for second variant of task 2

# Homework 1 - Task 1 - FIZBUZZ game

number = int(input("FIZZBUZZ GAME - Please enter a number:"))

for i in range(number + 1):
    if i == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FIZZBUZZ")
    elif i % 3 == 0:
        print(i, "FIZZ")
    elif i % 5 == 0:
        print(i, "BUZZ")
    else:
        print(i, "is just a booring number...")

# Task 2 - n-th Prime number --------------------------------------

nthPrime = int(input("\nEnter which n-th Prime number you want to be printed: "))
checker = 0
num = 2
lastPrime = 0

while checker != nthPrime:
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
            break
    if count == 0:
        checker += 1
        lastPrime = num
    num += 1
print(nthPrime, "th prime number is: ", lastPrime, "\n")

# Task 2 - using sympy library
print(sympy.prime(int(input("Enter which n-th Prime number you want to be printed: "))))
