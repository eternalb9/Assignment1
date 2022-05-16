numbers = (1,2,3,4,5,6,7,8,9)
even=odd=0
for i in numbers:
    if i % 2 == 0:
        even = even + 1
        
    
    else:
        odd=odd + 1
        
            

print("Number of even terms ",even)
print("Number of odd terms ",odd)        