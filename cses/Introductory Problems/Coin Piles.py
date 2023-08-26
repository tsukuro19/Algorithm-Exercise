# Function to check if both piles can be emptied
def can_empty_piles(a, b):
    if (a + b) % 3 == 0 and  2*a >= b and 2*b >= a:
        return "YES"
    else:
        return "NO"

# Read the number of tests
t = int(input())

# Iterate for each test case
for _ in range(t):
    # Read the values of a and b
    a, b = map(int, input().split())

    # Check if both piles can be emptied and print the result
    print(can_empty_piles(a, b))