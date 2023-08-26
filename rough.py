import sys
from src.logger import *
from src.exception import *


def multiply(a, b):
    if a == 0 or b == 0:
        raise ValueError
    else:
        return a*b


if __name__ == '__main__':
    try:
        number = multiply(0, 5)
    except Exception as e:
        CustomException(e, sys)
        logging.info(e)
