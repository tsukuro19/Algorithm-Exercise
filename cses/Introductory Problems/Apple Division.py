def divide_apples(apples, n, group1_sum, group2_sum, current_index):
    if current_index == n:
        # Reached the end, return the absolute difference between the two group sums
        return abs(group1_sum - group2_sum)
    
    # Recursive case: include the current apple in group 1
    diff1 = divide_apples(apples, n, group1_sum + apples[current_index], group2_sum, current_index + 1)
    
    # Recursive case: include the current apple in group 2
    diff2 = divide_apples(apples, n, group1_sum, group2_sum + apples[current_index], current_index + 1)
    
    # Return the minimum difference between the two cases
    return min(diff1, diff2)

# Read the input
n = int(input())
apples = list(map(int, input().split()))

# Call the divide_apples function to calculate the minimum difference
min_diff = divide_apples(apples, n, 0, 0, 0)

# Print the minimum difference
print(min_diff)