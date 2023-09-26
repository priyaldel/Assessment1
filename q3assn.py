def dectooct(decimal_num):
    octal_num=oct(decimal_num)
    return octal_num

def reverseint(number):
    rev_num = int(str(number)[::-1])
    return rev_num

def fibonacci(n):
    if n <=0:
        return []
    elif n ==1:
        return [0]
    elif n ==2:
        return [0,1]
    else:
        fib_seq = fibonacci(n -1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
    
def nthvalue(n):
    if n <=0:
        return None
    elif n ==1:
        return 0
    elif n ==2:
        return 1
    else:
        a,b = 0,1
        for _ in range(n - 2):
            a,b = b, a+b
        return a+b
    
while True:
    print("Choose an option:")
    print("1.Covert decimal to octal")
    print("2.Reverse an integer")
    print("3.Print fibonacci using recursion")
    print("4.Return nth value from fibonacci")
    print("5.Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice ==1:
        decimal_num= int(input("Enter a decimal number: "))
        octal_num = dectooct(decimal_num)
        print(f"Octal is: {octal_num}")
        
    elif choice==2:
        number = int(input("Enter integer: "))
        rev_num = reverseint(number)
        print(f"Reverse int: {rev_num}")
        
    elif choice==3:
        n=int(input("Enter no. of fibonacci terms to generate: "))
        fib_seq=fibonacci(n)
        print(fib_seq)
        
    elif choice==4:
        n = int(input("Enter position to find in fibonacci: "))
        nthval = nthvalue(n)
        print(nthval)
        
    elif choice ==5:
        break
    
    else:
        print("Invalid choice")