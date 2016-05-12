"""lic_check.sample."""


def hello(name):
    """respond hello.

    :rtype: str
    :return: "Hello `name`."

    :param str name: user name.

    >>> hello('Alice')
    'Hello, Alice.'
    """
    return 'Hello, {0}.'.format(name)


def bmi(height, weight):
    """Respond BMI.

    :rtype: float
    :return: Body mass index.

    :param float height: height (meters).
    :param float weight: weight (kilo grams).

    >>> bmi(1.68, 67.0)
    23.738662131519277

    >>> bmi(0, 67.0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero
    """
    return weight / height ** 2
