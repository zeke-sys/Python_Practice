# This file is part of the Python Practice repository.
# This function calculates the power of a number modulo m using recursion.
# This is Algorithm 4 from Rosen's Discrete Mathematics, 7th Edition, p. 363.

def mpower(b, n, m): # Recursive function to calculate b^n mod m
    print(f"mpower({b}, {n}, {m})")
    if n == 0: # Base case: any number to the power of 0 is 1
        print(f"returning 1 for base case")
        return 1
    elif n % 2 == 0: # If n is even
        half_power = mpower(b, n // 2, m) # Calculate b^(n/2) mod m
        result = (half_power * half_power) % m # Square the result and take mod m
        print(f"even n: {n}, half_power: {half_power}, result: {result}")
        return result
    else: # If n is odd
        half_power = mpower(b, n // 2, m) # Calculate b^(n//2) mod m
        result = (half_power * half_power * b) % m # Square the result and multiply by b, then take mod m
        print(f"odd n: {n}, half_power: {half_power}, result: {result}")
        return result

# Example usage
b = 2
n = 10
m = 7

print(f"Calculating {b}^{n} mod {m}")
result = mpower(b, n, m)

