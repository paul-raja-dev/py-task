def reverse_number(n):
    rev = int(str(abs(n))[::-1])
    return -rev if n < 0 else rev

print(reverse_number(123))
