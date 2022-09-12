def is_fizz_or_buzz(x: int):
    if x < 1 or x > 1000:
        return ''
    
    if x%3 == 0 and x%5 == 0:
        return 'FizzBuzz'
    elif x%3 == 0:
        return 'Fizz'
    elif x%5 ==0:
        return 'Buzz'
    
    return ''