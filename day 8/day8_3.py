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

user_no = int(input("enter the no"))
result = prime_num(user_no)        
print(result)