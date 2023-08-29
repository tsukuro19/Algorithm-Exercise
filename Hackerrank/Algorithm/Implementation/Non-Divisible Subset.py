def nonDivisibleSubset(k, S):
    remainders = [0] * k

    for num in S:
        remainders[num % k] += 1

    count = min(remainders[0], 1)  # Include at most one number divisible by k

    for i in range(1, k//2 + 1):
        if i != k - i:
            # If i is not equal to k - i, we are considering pairs of distinct remainders
            # Choose the maximum count between remainders[i] and remainders[k-i]
            count += max(remainders[i], remainders[k-i])
        else:
            # If i is equal to k - i, we are considering a single remainder
            # Include at most one number with this remainder, so choose the minimum between remainders[i] and 1
            count += min(remainders[i], 1)

    return count


# Example usage
n, k = map(int, input().split())
S = list(map(int, input().split()))

result = nonDivisibleSubset(k, S)
print(result)