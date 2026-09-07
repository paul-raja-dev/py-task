def reverse_three_digit(n):
    hundreds = abs(n) // 100
    tens = (abs(n) // 10) % 10
    ones = abs(n) % 10
    return ones * 100 + tens * 10 + hundreds

print(reverse_three_digit(738))
