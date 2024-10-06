def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot_sum = get_aliquot_sum(number)
    if aliquot_sum == 1 or aliquot_sum < number:
        return "deficient"
    return "perfect" if aliquot_sum == number else "abundant"


def get_aliquot_sum(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = [1]
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)

