def evnum():
   for num in range(1,21):
      if num %2 == 0:
         print(num)
    
evnum()    


# 2nd program
def sum_numbers():
    total_sum = 0  

    for i in range(5): 
        num = float(input(f"Enter number {i + 1}: ")) 

        if num > 0:  
            total_sum += num  

    print("Total sum of positive numbers:", total_sum)


sum_numbers()
