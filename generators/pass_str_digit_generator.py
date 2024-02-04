import random
import string


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    print(result_str)


get_random_string(20)
