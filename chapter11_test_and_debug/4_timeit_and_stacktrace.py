import timeit
import traceback
import logging

logging.basicConfig(filename='./tmp/example.log', format='%(asctime)s %(levelname)s %(message)s')

print(timeit.timeit('"test" in "This is a test."'))

print(timeit.repeat('"test" in "This is a test."'))

t = timeit.Timer('char in text', setup='text = "This is a test."; char = "test"')
print(t.timeit())

s = """
try:
    "This is a test".__bool__
except AttributeError:
    pass
"""

print(timeit.timeit(stmt=s))


def hoge():
    tuple()[0]

try:
    hoge()
except IndexError:
    print('--- Exception occurred ---')
    traceback.print_exc(limit=None)


try:
    tuple()[0]
except IndexError:
    logging.error(traceback.format_exc())
    raise

