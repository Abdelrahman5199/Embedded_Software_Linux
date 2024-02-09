def Count_Number(lst, num):
    count = 0
    
    for element in lst:
        if element == num:
            count += 1
            
    return count
lst = [1, 4, 6, 7, 4]
num = 4
result = Count_Number(lst, num)
print("The count number of", num, "in the list is: ",result)
         