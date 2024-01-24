print("the number identifer")

num = int(input("enter the number: "))

if num ==0:
    print("its zero")
if num %2 == 0 and num<0 :
    print("nagative even")
elif num %2==0 and num > 0:
    print("positive even")
elif num%2!=0 and num < 0 :
    print("nagetive odd")
elif num%2!=0 and num > 0 :
    print("positive odd")
