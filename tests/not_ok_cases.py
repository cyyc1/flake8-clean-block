case_1_src = """a = 2
for i in range(5):
    a += 1
print(a)
"""
case_1 = (case_1_src, [3])  # "3" means the violation happens on Line 3


case_1a_src = """
a = 2
for i in range(5):
    a += 1
    for j in range(4):
        b +=1
    a += b
print(a)
print(b)
"""
case_1a = (case_1a_src, [6, 7])  # the violation happens on Lines 6 & 7


case_1b_src = """
for i in range(5): a += 2
print(a)
"""
case_1b = (case_1b_src, [2])


case_2_src = """
if a == 1:
    print(a)
if b == 2:
    print(b)
for i in (1, 3, 5, 10):
    b += i
while True:
    print('a')
"""
case_2 = [case_2_src, [3, 5, 7]]


case_2a_src = """
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
case_2a = [case_2a_src, [7, 9, 11]]


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


case_5_src = """
if x < 5:
    print(x)
elif y == 2:
    print(y)
else:
    raise ValueError
return 2
"""
case_5 = (case_5_src, [7])


case_5a_src = """
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
case_5a = [case_5a_src, [12, 15]]


case_6_src = """
while True:
    print(1)
print(2)
"""
case_6 = [case_6_src, [3]]


case_6a_src = """
while True: print(1)
print(2)"""
case_6a = [case_6a_src, [2]]


case_7_src = """
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
case_7 = [case_7_src, [7]]


case_7a_src = """
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
case_7a = [case_7a_src, [7, 11, 15]]


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


case_10_src = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)
print(data)
"""
case_10 = [case_10_src, [3]]


case_10a_src = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)
    for ii in range(10):
        print(ii)
print(data)
"""
case_10a = [case_10a_src, [5]]


case_10b_src = """import pickle
with open('filename.txt', 'r') as fp:
    data = pickle.load(fp)
    for ii in range(10):
        print(ii)
    xyz = 1
print(data)
"""
case_10b = [case_10b_src, [5, 6]]


def collect_all_cases():
    return (
        case_1,
        case_1a,
        case_1b,
        case_2,
        case_2a,
        case_3,
        case_4,
        case_5,
        case_5a,
        case_6,
        case_6a,
        case_7,
        case_7a,
        case_8,
        case_9,
        case_10,
        case_10a,
        case_10b,
    )
