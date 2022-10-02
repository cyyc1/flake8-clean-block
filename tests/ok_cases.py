case_0 = ''  # trivial case: no code at all


case_1a = """a = 2
for i in range(5):
    a += 1

print(a)
"""

case_1b = case_1a.replace('\n\n', '\n\n\n\n\n')  # OK to have more blank lines


case_1c = case_1a.replace(  # OK to have comments on blank lines
    '\n\n',
    '\n# END OF "IF" BLOCK\n',
)


case_1d = case_1a.replace('\n\n', '\n  \n')  # OK to have spaces on blank lines


case_1e = """for i in range(5):
    a += 2"""  # no newline at the end


case_1f = 'for i in range(5): a += 2'


case_1g = """
for i in range(5): a += 2

print(a)
"""


case_1h = """
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    for n in range(5):
                        for o in range(5):
                            for p in range(5):
                                for q in range(5):
                                    for r in range(5):
                                        for s in range(5):
                                            for t in range(5):
                                                for u in range(5):
                                                    for v in range(5):
                                                        for w in range(5):
                                                            for x in range(5):
                                                                print(1)

print(2)
"""


case_2a = """
if a == 1:
    print(a)
elif a == 2:
    print(a)
else:
    print(a)

if b == 2:
    print(b)

for i in range(2):
    b += i

while True:
    print('a')
"""


case_2b = case_2a.replace('\n\n', '\n# SOME COMMENT\n')


case_3a = """a = 2
for i in range(5):
    for j in range(3):
        a += j

    a += i

print(a)
"""


case_3b = case_3a.replace(  # OK to have comments on blank lines
    '\n\n',
    '\n# END OF INDENTED BLOCK\n',
)


case_4 = """
if 3 >= 2:
    if 2 > 1:
        print('yes')

    print('no')

print('good')
"""


case_5a = """
if x < 5:
    print(x)
elif y == 2:
    print(y)
else:
    raise ValueError

return 2
"""


case_5b = """
if x < 5:
    print(x)
    while z > 0:
        print(z)
        z -= 1  # it's OK to have no blank line after this line
elif y == 2:
    print(y)
    for k in range(10):
        print(k)
        for l in range(2):
            l += 2  # needs to have a blank line behind this line

        bb = 1  # no need for a blank line behind this line
else:
    raise ValueError

return 2
"""


case_5c = """
if a == 'a':
    depth += 1
elif b == 'b':
    depth -= 1

j += 1
"""


case_6 = """
while True:
    print(1)

print(2)
"""


case_7a = """
try:
    f = open('myfile.txt')
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
"""


case_7b = """
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    for aa in range(2):
        bb += 2

    print(aa)
except OSError as err:
    print("OS error: {0}".format(err))
    if a == 1:
        b = a + 1

    b = 2
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
"""


case_7c = """
try:
    a = 1
except TypeError as err:
    print(err)
except ValueError as valErr:
    print(valErr)
finally:
    print(2)
"""


case_8 = """
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        for k in range(2):
            print(k)

        f.close()
"""


case_9 = """
try:
    raise KeyboardInterrupt
finally:
    for kk in range(5):
        abc += 1

    print('Hello world!')"""


case_10a = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)

print(data)
"""


case_10b = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)
    for ii in range(10):
        print(ii)

print(data)
"""


case_10c = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)
    for ii in range(10):
        print(ii)

    xyz = 1

print(data)
"""


case_11a = """
def some_func(arg1: list, arg2: list) -> int:
    for i in range(len(arg1)):
        for j in range(len(arg2)):
            print(i)

        print(j)

    return 5

if True:
    some_func([1, 2, 3], [2, 3])

print('Good morning')
"""


case_11b = """
class MyClass:
    def __init__(self, arg1):
        if arg1 == 2:
            self.my_attr = 1

        self.my_attr = 2

    @classmethod
    def do_something(cls, arg1):
        for i in range(20):
            print(i)

        print(arg1)

    def do_something_else(self, arg1, arg2):
        if 5 in arg1:
            print(arg1)

        for j in arg2:
            foo = 3 + 4

        return 5


"""


# This is OK, because it's out of the scope of this plugin.
# It can be caught by E3 in pycodestyle:
# https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes
case_99a = """
def some_func(arg1, arg2):
    print(2)
a = 2
"""


# Similar to Case 99a, this is also OK, because it's out of the scope of this
# plugin.
case_99b = """
def some_func(arg1, arg2):
    return arg1 + arg2
a = 3
"""


def collect_all_cases():
    return (
        case_0,
        case_1a,
        case_1b,
        case_1c,
        case_1d,
        case_1e,
        case_1f,
        case_1g,
        case_1h,
        case_2a,
        case_2b,
        case_3a,
        case_3b,
        case_4,
        case_5a,
        case_5b,
        case_5c,
        case_6,
        case_7a,
        case_7b,
        case_7c,
        case_8,
        case_9,
        case_10a,
        case_10b,
        case_10c,
        case_11a,
        case_11b,
        case_99a,
        case_99b,
    )
