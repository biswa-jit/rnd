"""
Modify percentage value to gain insight.
e.g: In case greater chance of exception make the value .1 (if takes less time)
			 lesser chance of exception make the value .9 (if and exceptio both take similar time)

"""
import timeit

SETUP = """
import random
with open('/usr/share/dict/words', 'r') as fp:
    words = [word.strip() for word in fp.readlines()]
percentage = int(len(words) *.9)
my_dict = dict([(w, w) for w in random.sample(words, percentage)])
counter = 0
"""

LOOP_IF = """
word = random.choice(words)
if word in my_dict:
    counter += len(my_dict[word])
"""

LOOP_EXCEPT = """
word = random.choice(words)
try:
    counter += len(my_dict[word])
except KeyError:
    pass
"""


if __name__ == '__main__':
    if_time = timeit.Timer(LOOP_IF, setup=SETUP)
    except_time = timeit.Timer(LOOP_EXCEPT, setup=SETUP)
    number = 1000000
    min_if_time = min(if_time.repeat(number=number))
    min_except_time = min(except_time.repeat(number=number))

    print """using if statement:
    minimum: {}
    per_lookup: {}
    """.format(min_if_time, min_if_time / number)

    print """using exception:
    minimum: {}
    per_lookup: {}
    """.format(min_except_time, min_except_time / number)
