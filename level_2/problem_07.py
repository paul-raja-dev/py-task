def odd_numbers_sum_seven():
    for i in range(11, 100, 2):
        tens = i // 10
        ones = i % 10
        if tens + ones == 7:
            print(i)

odd_numbers_sum_seven()
