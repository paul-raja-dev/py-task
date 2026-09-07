def check_sum_of_digits(n):
    total = sum(int(d) for d in str(abs(n)))
    if total == 14:
        return "Sum of Digits is 14"
    else:
        return "Sum of Digits is not 14"

print(check_sum_of_digits(59))
