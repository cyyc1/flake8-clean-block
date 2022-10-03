case_1a_src = """a = 2
for i in range(5):
    a += 1
print(a)
"""
case_1a = (case_1a_src, [3])  # "3" means the violation happens on Line 3


case_1b_src = """
a = 2
for i in range(5):
    a += 1
    for j in range(4):
        b +=1
    a += b
print(a)
print(b)
"""
case_1b = (case_1b_src, [6, 7])  # the violation happens on Lines 6 & 7


case_1c_src = """
for i in range(5): a += 2
print(a)
"""
case_1c = (case_1c_src, [2])


case_1d_src = """
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
case_1d = (case_1d_src, [18])


case_1e_src = """
def some_func(arg1):
    if arg1:
        return 2
    return 1
"""
case_1e = [case_1e_src, [4]]


case_2a_src = """
if a == 1:
    print(a)
if b == 2:
    print(b)
for i in (1, 3, 5, 10):
    b += i
while True:
    print('a')
"""
case_2a = [case_2a_src, [3, 5, 7]]


case_2b_src = """
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
case_2b = [case_2b_src, [7, 9, 11]]


case_3_src = """a = 2
for i in range(5):
    for j in range(3):
        a += j

    a += i
print(a)
"""
case_3 = (case_3_src, [6])


case_4_src = """
if 3 >= 2:
    if 2 > 1:
        print('yes')
    print('no')

print('good')
"""
case_4 = (case_4_src, [4])


case_5a_src = """
if x < 5:
    print(x)
elif y == 2:
    print(y)
else:
    raise ValueError
return 2
"""
case_5a = (case_5a_src, [7])


case_5b_src = """
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
            l += 2  # <-- violation here
        bb = 1  # no need for a blank line behind this line
else:
    raise ValueError  # <-- violation here
return 2
"""
case_5b = [case_5b_src, [12, 15]]


case_5c_src = """
if a == 'a':
    depth += 1
elif b == 'b':
    depth -= 1
j += 1
"""
case_5c = [case_5c_src, [5]]


case_6a_src = """
while True:
    print(1)
print(2)
"""
case_6a = [case_6a_src, [3]]


case_6b_src = """
while True: print(1)
print(2)"""
case_6b = [case_6b_src, [2]]


case_7a_src = """
try:
    f = open('myfile.txt')
except OSError as err:
    print(2)
    if a == 1:
        b = a + 1
    b = 2
except ValueError:
    print("asdf")
"""
case_7a = [case_7a_src, [7]]


case_7b_src = """
try:
    f = open('myfile.txt')
except OSError as err:
    print(2)
    if a == 1:
        b = a + 1
    b = 2
except ValueError:
    for kk in range(5):
        kk += 1
    print("asdf")
finally:
    if b == 2:
        print(b)
    print('a')
"""
case_7b = [case_7b_src, [7, 11, 15]]


case_8_src = """
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        for k in range(2):
            print(k)  # <-- violation here
        f.close()
"""
case_8 = [case_8_src, [10]]


case_9_src = """
try:
    raise KeyboardInterrupt
finally:
    for kk in range(5):
        abc += 1
    print('Hello world!')"""
case_9 = [case_9_src, [6]]


case_10a_src = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)
print(data)
"""
case_10a = [case_10a_src, [3]]


case_10b_src = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)
    for ii in range(10):
        print(ii)
print(data)
"""
case_10b = [case_10b_src, [5]]


case_10c_src = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)
    for ii in range(10):
        print(ii)
    xyz = 1
print(data)
"""
case_10c = [case_10c_src, [5, 6]]


case_11a_src = """
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
case_11a = [case_11a_src, [5, 6, 10]]


case_11b_src = """
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
case_11b = [case_11b_src, [5, 11, 16, 18]]


def collect_all_cases():
    return (
        case_1a,
        case_1b,
        case_1c,
        case_1d,
        case_1e,
        case_2a,
        case_2b,
        case_3,
        case_4,
        case_5a,
        case_5b,
        case_5c,
        case_6a,
        case_6b,
        case_7a,
        case_7b,
        case_8,
        case_9,
        case_10a,
        case_10b,
        case_10c,
        case_11a,
        case_11b,
    )
