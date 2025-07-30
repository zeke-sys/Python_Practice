#This function calculates the sum of numbers in a sequence (Rosen Exercise 29, p. 169)

def summation(num1, last_num):
    total = 0
    for k in range(num1, last_num + 1):
        total += k + 1 #total starts at 0 and adds every number after plus 1
    return total

this_sum = summation(1, 5) #calling function and passing given arguments
print("Sum =", this_sum)