import time

# The two functions compare two different implementations of a recursive algorithm with a Fibonacci-like
# structure to highlight the importance of avoiding redundant computations
# Also shows that even slight changes in code (aka H(n)) can reduce runtime quite a bit
# Adding I(n) to refactor G(n) without memoization

# G(n) is highly inefficient due to repeated recursive calls without memoization or iteration, 
# resulting in exponential time complexity
def G(n):
    if n <= 2:
        return n
    return G(n-2) * G(n-2) - G(n-1) * G(n-3) # calculates the same values many times

g_start = time.time() # start time
print('G of 25', G(25), '\n')
g_end = time.time()

g_total_time = g_end - g_start
print('G time', g_total_time, '\n')

def H(n): # slightly better as it computes G(n-2) once and stores it in x. Still redundant!
    if n <= 2:
        return n
    x = G(n-2)
    return x * x - G(n-1) * G(n-3)

h_start = time.time()
print('H of 25', H(25), '\n')
h_end = time.time()

h_total_time = h_end - h_start
print('H time', h_total_time, '\n')

print("----------------------")
print("G(n) being refactored into I(n) without memoization.\n")


# Factoring to have subresults shared within calls
# G(n-2) is no longer being called twice and recursed independently
# I(n) allows each recursive value to be computed once and reused
def I(n):
    if n <= 2:
        return n
    
    i_n2 = I(n - 2)
    i_n1 = I(n - 1)
    i_n3 = I(n - 3)

    return i_n2 * i_n2 - i_n1 * i_n3

i_start = time.time()
print('I of 25', I(25), '\n')
i_end = time.time()

i_total_time = i_end - i_start
print('I time', i_total_time, '\n')

print("\nWill try memoization or loop iteration next to try to eliminate repeated calls across different levels.")