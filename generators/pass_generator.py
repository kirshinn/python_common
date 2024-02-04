import random
import string

password = ''.join(random.choice(string.printable) for i in range(20))
print("Random password is:", password)
