from itertools import permutations

# Read the input string
input_string = input()

# Find all permutations of the characters in the input string
permutations_list = sorted(set(permutations(input_string)))

# Print the number of strings and the strings themselves
print(len(permutations_list))
for permutation in permutations_list:
    print(''.join(permutation))