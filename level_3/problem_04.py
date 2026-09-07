def check_prime(n):
    if n <= 1:
        return "Number is not Prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Number is not Prime"
    return "Number is Prime"

print(check_prime(61))
