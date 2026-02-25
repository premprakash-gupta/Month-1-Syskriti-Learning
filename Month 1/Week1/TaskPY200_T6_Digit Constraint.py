limit = int(input("Enter number N:"))


for i in range(1000, limit):
    number =i
    sum =0
    count_three = 0
    contains_zero = False

    
    #while loop
    while(number > 0):
        n = number%10
        number = number//10
        if(n==0):
            contains_zero = True
            break
        if(n==3):
            count_three=count_three+1
            
        sum =sum+n
        
    if(not contains_zero and count_three==2 and sum==7):
        print(i)
        quit()
       
    
        
print(-1)
