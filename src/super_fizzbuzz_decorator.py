def fizzbuzz(fizz_str: str, *dividers):
    def inner_function(func):
        def wrapper(num: int):
            for divider in dividers:
                if num % divider != 0:
                    return func(num)
            return fizz_str
        return wrapper
    return inner_function


###############################################


@fizzbuzz('FizzFizzBuzzBuzz', 9, 25)
@fizzbuzz('FizzFizz', 9)
@fizzbuzz('BuzzBuzz', 25)
@fizzbuzz('FizzBuzz', 3, 5)
@fizzbuzz('Fizz', 3)
@fizzbuzz('Buzz', 5)
def super_fizzbuzz(num: int):
    return 'NoFizzBuzz'


# print(super_fizzbuzz(15))