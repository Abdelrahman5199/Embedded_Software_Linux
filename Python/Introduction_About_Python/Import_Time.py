import time

# Creating list of numbers 
number_list = list(range(1, 100009))

#Creating set of numbers
number_set = set(number_list)

#Searching number in List
start_time = time.time()
print(100000 in number_list)
end_time = time.time()
print("Time to taken to search", end_time - start_time, "Seconds")

#Searching number in List
start_time = time.time()
print(100000 in number_set)
end_time = time.time()
print("Time to taken to search", end_time - start_time, "Seconds")