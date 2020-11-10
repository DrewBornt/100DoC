def prime_check(number):
    i = 2
    prime = False
    while (not prime and i < number):
        if number % i == 0:
            print(f"{number} is not prime")
            break
        else:
            i+=1
    
    if ( i == number):
        print(f"{number} is prime!")

prime_check(int(input("Enter a number to check if it is prime: ")))