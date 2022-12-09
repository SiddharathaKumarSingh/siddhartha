while True:
    try:
        n=int(input())
        def fibonacci(n):
            c=0
            i=1
            j=1
            if n<0:
                print('enter positive integer')
            elif n==0 or n==1:
                return(" Valid")
            elif n>0:    
                while n>c:
                    c=i+j
                    i=j
                    j=c
                if c==n:
                    return(" Valid")
                else:
                    return("Invalid")
        print(fibonacci(n))
        a=input(str("you want to check one more Time(yes/no):  "))
        if a !="yes":
            break
    except ValueError:
        print("input a Number ")
