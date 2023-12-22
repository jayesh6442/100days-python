#prime number checker

def prime_num(number):
    is_prime = True
for i in range(2,number):
    if number %i==0:
        is_prime=False
    if is_prime:
        print("prime number")
    else:
            print("not a prime")

prime_num(6)        