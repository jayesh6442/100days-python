#prime number checker
def prime_np(number):
    is_prime = True
    for i in range(2,number):
        if number % i ==0:
            is_prime= False
    if is_prime:
        print("prime")
    else:
        print("not prime")
user_no = int(input("enter the no: "))
result = prime_np(user_no)        
