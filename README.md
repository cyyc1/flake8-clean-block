# flake8-clean-block

This is a [flake8](https://flake8.pycqa.org/en/latest/) plugin that enforces a blank line after `if`/`for`/`while`/`with`/`try` blocks in Python code.

## Installation

```bash
pip install flake8-clean-block
```

## Violation codes

There is one violation code that this plugin reports:

| Code      | Description                                            |
| --------- | ------------------------------------------------------ |
| CLB100    | no blank line after the end of an indented block       |


## Style examples

### _Wrong_

This plugin considers the following styles as wrong:

```python
for i in range(5):
    print(i)
some_var = 2
```

```python
for i in range(5):
    print(i)
if k == 2:
    print(k)
else:
    print("k")
for j in range(5):
    print(j)
```

```python
for i in range(5): a += i
print(a)
```

```python
with open('filename.txt', 'r') as fp:
    content = fp.readlines()
print(content)
```

### _Correct_

Correspondingly, here are the correct styles, because they are easier to read and less error-prone:

```python
for i in range(5):
    print(i)

some_var = 2
```

```python
for i in range(5):
    print(i)

if k == 2:
    print(k)
else:
    print("k")

for j in range(5):
    print(j)
```

```python
for i in range(5): a += i

print(a)
```

```python
with open('filename.txt', 'r') as fp:
    content = fp.readlines()

print(content)
```

## Rationale

When two lines belonging to different indentation level are right next to each other, it's difficult to read.  Additionally, accidentally hitting the "tab" key on the outer line leads to subtle and hard-to-find bugs (and vice versa).

Therefore, it's better that we add at least one blank line between lines of different indentation levels.

