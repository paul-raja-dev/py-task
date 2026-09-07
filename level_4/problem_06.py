def reverse_two_digit(n):
    tens = abs(n) // 10
    ones = abs(n) % 10
    return ones * 10 + tens

print(reverse_two_digit(73))
