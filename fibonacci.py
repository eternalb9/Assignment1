
first,second=0,1
count=0
terms = int(input("Enter no of terms  "))

if terms<=0:
    print("Enter a valid no of terms")

elif terms==1:
    print("The fibonacci series is",first)   

else:
    while count<terms:
        print(first, end=" ")
        temp= first + second
        first = second
        second = temp
        count+=1
                 