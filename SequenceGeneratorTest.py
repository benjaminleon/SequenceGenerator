import sys
import re
from SequenceGenerator import SequenceGenerator

generator = SequenceGenerator()
generator.generate()
sequence = generator.sequence

for i in range(0, 10000):
    s = "{}".format(i)
    s = "0" * (4 - len(s)) + s
    if s not in sequence:
        print("Failed! {} is missing.".format(s))
        exit(1)

print("Passed! Valid sequence.")
