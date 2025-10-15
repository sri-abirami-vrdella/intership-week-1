"""check if each integer from 1 to n is even or odd , and check if prime and skip if the
 number is divisible by 5."""

n=int(input("Enter a positive integer: "))
if n>0: #check if positive
    for i in range(1,n+1):
        if i==1: #1 is neither prime not composite
            print("1-> odd")
        elif i%5==0: # skip multiples of five
            print("skipped")
            continue
        elif i%2==0: #check if even
            x=2 # all numbers divisible by 1
            fl=1
            while x<i: # all number divisible by itself
                if i%x==0: #check if prime
                    print(f"{i}->Even")
                    fl=0
                    break
                x+=1
            if fl==0:
                continue
            print(f"{i}->Even(prime)")
        else: #if odd
            x = 2
            fl=1
            while x <i: #all number divisibke by it self
                if i % x == 0: #check if prime
                    print(f"{i}->odd")
                    fl=0
                    break
                x+=1
            if fl==0:
                continue
            print(f"{i}->odd(prime)")
else:
    print("enter a positive integer")
