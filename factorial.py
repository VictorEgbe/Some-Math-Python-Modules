'''
The Factorial function
Includes conditions to ensure the user enters a number
'''


def factorial(number):
    """Calculates the factorial of a number """
    p = 1
    x = 2
    str_number = str(number)

    if not type(number) == int:
        try:
            raise ValueError('Invalid Input. Please enter a positive integer.')
        except ValueError as e:
            return e

    if not str_number.isnumeric():  # or if not type(number) == int:
        try:
            raise Exception('You did not enter a valid number!')
        except Exception as error:
            return error

    while x <= number:
        p = p * x
        x += 1
    return f'{number}! = {p}'


# print(factorial(10))
