
def factors(number):
    answer = []
    for num in range(1, number + 1):
        if number % num == 0:
            answer.append(num)
    return answer


def is_prime_number(number):
    if len(factors(number)) == 2:
        return True
    return False


def prime_factors(number):
    prime_factors_list = set()
    for factor in factors(number):
        if is_prime_number(factor):
            prime_factors_list.add(factor)
    if prime_factors_list == set():
        return f'{number} has no prime factors'
    return prime_factors_list


def prime_numbers_range(start, stop):
    range_list = []
    for number in range(start, stop + 1):
        if is_prime_number(number):
            range_list.append(number)
    return range_list

