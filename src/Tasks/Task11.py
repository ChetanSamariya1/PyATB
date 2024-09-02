# Fibonacci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

# Input from the user
n = int(input("Enter the number of terms: \n"))

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci Series:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
