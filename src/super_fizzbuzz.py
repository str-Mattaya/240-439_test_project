class BaseCondition:

    def __init__(self, *dividers):
        self.dividers = dividers

    def call(self, num: int):
        for divider in self.dividers:
            if num % divider != 0:
                return None
        return self.get_string()

    def get_string(self):
        return 'NoFizzBuzz'

class FizzCondition(BaseCondition):

    def __init__(self):
        super().__init__(3)
    
    def get_string(self):
        return 'Fizz'

class BuzzCondition(BaseCondition):

    def __init__(self):
        super().__init__(5)
    
    def get_string(self):
        return 'Buzz'

class FizzBuzzCondition(BaseCondition):

    def __init__(self):
        super().__init__(3,5)
    
    def get_string(self):
        return 'FizzBuzz'

class FizzFizzCondition(BaseCondition):

    def __init__(self):
        super().__init__(9)
    
    def get_string(self):
        return 'FizzFizz'

class BuzzBuzzCondition(BaseCondition):

    def __init__(self):
        super().__init__(25)
    
    def get_string(self):
        return 'BuzzBuzz'

class FizzFizzBuzzBuzzCondition(BaseCondition):

    def __init__(self):
        super().__init__(9,25)
    
    def get_string(self):
        return 'FizzFizzBuzzBuzz'


#############################################

def super_fizzbuzz(num: int) -> str:

    conditions: list[BaseCondition] = [
        FizzFizzBuzzBuzzCondition(),
        BuzzBuzzCondition(),
        FizzFizzCondition(),
        FizzBuzzCondition(),
        BuzzCondition(),
        FizzCondition(),
        BaseCondition(1)
    ]

    for condition in conditions:
        fizzbuzz = condition.call(num)
        if not fizzbuzz is None:
            return fizzbuzz


# print(super_fizzbuzz(15))