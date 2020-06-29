num = int(input("What is the number: "))

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//1, "is", num)
            break
        else:
            print(num, "is a prime number")

    else:
        print("It is not a prime number")