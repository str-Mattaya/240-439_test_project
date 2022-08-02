def is_prime_list(numbers):
    for num in numbers:
        # check if num < 0
        if num < 0:
            num = -num

        # 0 and 1 is not prime
        if num < 2:
            return False

        # check prime for num >= 2
        for n in range(2, num):
            if num % n == 0:
                return False
    return True
