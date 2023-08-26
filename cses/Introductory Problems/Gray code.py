def generate_gray_code(n):
    # Base case
    if n == 1:
        return ['0', '1']
    
    # Recursive case
    prev_gray_code = generate_gray_code(n - 1)
    
    gray_code = []
    
    # Append '0' to the front of each code in the previous gray code sequence
    for code in prev_gray_code:
        gray_code.append('0' + code)
    
    # Reverse the previous gray code and append '1' to the front of each code
    for code in reversed(prev_gray_code):
        gray_code.append('1' + code)
    
    return gray_code


# Read the input value of n
n = int(input())

# Generate the Gray code sequence
gray_code_sequence = generate_gray_code(n)

# Print the Gray code sequence
for code in gray_code_sequence:
    print(code)