def count_zeros(n):
    count = 0
    for digit in str(abs(n)):
        if digit == '0':
            count += 1
    return count

print(count_zeros(100))
