# Python Notes

Notes based on everything covered in the `Python/` folder: variables, data types, operators, conditionals, loops, functions, lists, tuples, dictionaries, and object-oriented programming (the `self` concept).

## 1. Variables

A **variable** is a name that stores a value in memory so you can reuse it later.

```python
name = "Pranav"
age = 30
_subject = "123 jp nagar"
```

**Naming rules:**

1. Must start with a letter or underscore, followed by letters, numbers, or underscores (`1name = "John"` is invalid).
2. Cannot start with a number (`123 = 30` is invalid).
3. Can only contain letters, numbers, and underscores — no spaces (`student name` is invalid, use `student_name`).
4. Case sensitive — `name`, `NAME`, and `Name` are three different variables.
5. Cannot use Python keywords (`if`, `else`, `for`, `while`, `class`, `def`, `return`, `import`, `True`, `False`) as variable names.
6. Use meaningful names: `student_name = "pranav"` is far more readable than `a = "pranav"`.
7. Python convention is **snake_case** for variable names: `mentor_name`, not `mentorName` or `MentorName`.

**Real-world example:** A variable is like a labeled box. Instead of remembering "the value is in the third drawer," you just remember the label `student_name` and Python finds it for you.

## 2. Data Types & Typecasting

Python's core data types:

| Type | Example | Meaning |
|---|---|---|
| `int` | `23`, `87` | Whole numbers |
| `float` | `23.5`, `14.2` | Decimal numbers |
| `str` | `"Pranav"` | Text |
| `bool` | `True`, `False` | Logical yes/no |

Check a value's type with the built-in `type()` function:

```python
age = 22
print(type(age))   # <class 'int'>
```

**Typecasting** means converting one data type into another. This matters because `input()` always returns a **string**, even if the user types a number:

```python
num1 = input("Enter first number: ")
num2 = input("Enter Second number: ")
print(num1 + num2)   # "10" + "20" -> "1020" (string joining, not addition!)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
print(num1 + num2)   # 10 + 20 -> 30 (real addition)
```

**Real-world example:** Imagine a form field for "age" that's technically a text box. If you don't convert it to a number before doing math, "25" + "5" behaves like joining words, not adding numbers — exactly like sticking two puzzle pieces together instead of adding their values.

**Mini project from the repo (`hello.py`):** calculating the average of 3 subject marks entered as floats:

```python
mark1 = float(input("Enter first subject marks: "))
mark2 = float(input("Enter second subject marks: "))
mark3 = float(input("Enter  third  subject marks: "))
average = (mark1 + mark2 + mark3) / 3
print(average)
```

## 3. Operators

### Arithmetic operators

`+` addition, `-` subtraction, `*` multiplication, `/` division, `%` modulus (remainder).

```
10 / 2 -> 5   (quotient)
10 % 2 -> 0   (remainder)
```

**Real-world example:** if you have 10 candies and 3 friends, `10 // 3 = 3` candies each, and `10 % 3 = 1` candy left over — modulus tells you the leftover.

### Comparison operators

`==`, `!=`, `>`, `<`, `>=`, `<=` — compare two values and always return `True` or `False`.

### Logical operators — `and` / `or`

**AND truth table** (both sides must be true):

| A | B | Result |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**OR truth table** (at least one side must be true):

| A | B | Result |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

```python
a, b, c = 100, 200, 300
print(a >= b and c <= b)   # False and False -> False
```

**Real-world example:** A club entry rule "must be 18+ **and** have a ticket" uses `and` — both conditions must hold. "Free entry if you're a student **or** a staff member" uses `or` — either one is enough.

## 4. Conditional Statements

### `if`

Runs a block only when a condition is true.

```python
age = int(input("Enter your age:"))
if age >= 18:
    print("you are eligible to vote")
```

### `if / else`

Handles both the true and false paths.

```python
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

### `if / elif / else`

Checks multiple conditions in order and runs the **first** one that matches.

```python
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("The student has been failed in the examination")
```

### `match / case` (Python's switch statement)

Used instead of long `if/elif` chains when checking one variable against several fixed values — cleaner and easier to read.

```python
operator = input("Enter the operator(+ , - ,* ,/):")

match operator:
    case "+":
        print("Result =", num1 + num2)
    case "-":
        print("Result =", num1 - num2)
    case "*":
        print("Result =", num1 * num2)
    case "/":
        print("Result =", num1 / num2)
    case "_":
        print("Invalid Operator")
```

`case "_"` acts as the **default** — it runs if nothing else matched.

**Real-world example:** a vending machine checks which button you pressed (`match selection`) and dispenses the matching snack (`case`), instead of writing a long chain of "if button is A, else if button is B, else if..."

## 5. Loops

### `for` loop — use when you know how many times to repeat

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5

for i in range(2, 11, 2):
    print(i)   # 2, 4, 6, 8, 10 (range(start, stop, step))
```

### `while` loop — use when repetition depends on a condition, not a fixed count

```python
i = 1
while i <= 5:
    print(i)
    i = i + 1
```

Step by step: `i=1` → condition true → print → `i` becomes 2 → ... → `i=6` → condition false → loop stops.

### `for` vs `while`

| Feature | for loop | while loop |
|---|---|---|
| Iterations | Known | Unknown |
| Condition | Range or sequence | Pure condition based |
| Initialisation | Automatic | Manual |
| Update | Automatic | Manual (you must update it yourself) |
| Risk of infinite loop | Low | High (if you forget to update the condition) |
| Best use case | Fixed number of repetitions | Condition-driven repetition |

### Nested loops

A loop inside another loop. The inner loop finishes completely before the outer loop moves to its next step.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
# (0,0) (0,1) (1,0) (1,1) (2,0) (2,1)
```

### `break`, `continue`, `pass`

| Statement | What it does | Loop continues? | Current iteration |
|---|---|---|---|
| `break` | Exits the loop completely | No | Stops everything |
| `continue` | Skips the current iteration | Yes | Skips remainder |
| `pass` | Does nothing (placeholder) | Yes | Executes normally |

**`break` example — ATM PIN check (stop once correct):**

```python
correct_pin = "1234"
attempts = 0
max_attempt = 3

while attempts < max_attempt:
    pin = input("Enter the Pin: ")
    if pin == correct_pin:
        print("Login Successful")
        break
    else:
        print("Wrong pin")
        attempts = attempts + 1
```

**`continue` example — skip an absent student:**

```python
students = ["Ram", "John", "David", "Pranav"]
absent = "Pranav"

for student in students:
    if student == absent:
        continue
    print(student, "Present")
```

**`pass` example — placeholder for code you'll write later:**

```python
for num in range(1, 6):
    if num == 3:
        pass   # do nothing for now, but the line is syntactically required
    print(num)
```

**Real-world example:** `break` is like leaving a queue the moment you're served. `continue` is like skipping your turn and letting the next person go, but staying in the queue. `pass` is like reserving your spot in line without doing anything yet.

## 6. Functions

A **function** is a reusable block of code that performs a specific task.

```python
def greet():
    print("welcome to python")

greet()   # calling the function
```

- **Definition**: `def function_name():` — where the function's code lives.
- **Calling**: `function_name()` — where you actually run it.

### Parameters and arguments

```python
def greet(n):
    print("Hello", n)

greet("Pranav")
```

**Positional vs keyword arguments:**

```python
def student(phone_number, age):
    print(phone_number)
    print(age)

student(1000000000, 30)                       # positional: order matters
student(age=30, phone_number=1000000000)      # keyword: name matters, order doesn't
```

### `return` vs `print`

This is a key distinction:

```python
def addition_print(a, b):
    print(a + b)          # only displays the result, doesn't hand it back

def addition_return(a, b):
    return a + b          # sends the result back to whoever called it

result = addition_return(2, 3)   # result now holds 5, and can be reused
```

| | `print()` | `return` |
|---|---|---|
| Purpose | Display info to the user (debugging, logging) | Send a value back to the caller |
| Reusable? | No — the value is lost after printing | Yes — can be stored in a variable and reused |
| Performance | N/A | Faster for computed values used elsewhere |

**Real-world example:** `print()` is like a cashier reading your total out loud — you hear it, but can't do anything more with it. `return` is like the cashier handing you a receipt — you can use that number later (add it to a report, pass it to another calculation).

### `*args` and `**kwargs`

```python
def number(*numbers):
    print(numbers)

number(10, 20, 30)   # accepts any number of positional arguments -> (10, 20, 30)

def student(**details):
    print(details)

student(name="Pranav", age=12, city="Banglore")   # accepts any number of keyword arguments
```

- `*args` → collects any number of **positional** arguments into a tuple.
- `**kwargs` → collects any number of **keyword** arguments into a dictionary.

### Why use functions?

Code reusability, easier debugging, easier maintenance, less code duplication, better readability.

**Real-world example (`calculate_salary`):**

```python
def calculate_salary(hours):
    return hours * 500

salary = calculate_salary(8)
print(salary)   # 4000
```

Just like a payroll system: you feed in hours worked, and the same formula calculates salary for any employee, any number of times, without rewriting the math each time.

## 7. Lists

An **ordered**, **mutable** collection of items that can hold different data types.

**Properties:** ordered, mutable, allows duplicate values, indexed (starts from `0`).

```python
cricketers = ["Vk", "RS", "MSD"]

cricketers.append("Kl")     # add an item -> ["Vk", "RS", "MSD", "Kl"]
cricketers.remove("RS")     # remove an item -> ["Vk", "MSD", "Kl"]
print(cricketers[1])        # access by index -> "MSD"
```

**Summing values with a loop:**

```python
numbers = [25, 54, 67, 22]
total = 0
for num in numbers:
    total = total + num
print(total)   # 168
```

**Real-world example:** a list is like a numbered playlist — you can add a song, remove one, and songs can repeat, but the order and position (track 1, 2, 3...) always matters.

## 8. Tuples

An **ordered**, **immutable** collection — once created, it cannot be changed.

**Properties:** ordered, immutable, allows duplicates, indexed.

```python
colors = ("Red", "White", "Purple")
print(colors)
print(colors[1])          # "White"

numbers = (10, 20, 30, 40, 50, 10)
print(max(numbers))       # 50
print(min(numbers))       # 10
print(sum(numbers))       # 170
print(numbers.count(10))  # 2 (10 appears twice)
```

**Real-world example:** a tuple is like your date of birth — it's a fixed, ordered set of values (day, month, year) that should never change once recorded. Compare that to a list (like a shopping cart) which you're expected to keep editing.

## 9. Dictionaries

Stores data as **key-value pairs** — you look values up by key instead of by index.

**Properties:** mutable, keys are unique, values can be duplicated.

```python
student = {
    "name": ["Pranav", "MSD", "VK"],
    "age": "25",
    "city": "Banglore"
}

print(student["name"][1])   # "MSD"

student.update({"age": "23"})   # update an existing key
print(student)

student.pop("city")             # remove a key
print(student)
```

**Real-world example:** a dictionary is like a contact card — you don't say "give me the 3rd field," you say "give me the phone number" (the key), and it returns the value directly.

## 10. Object-Oriented Programming — the `self` concept

This is the core idea behind classes in Python, based on the `class/` folder (`calulator.py`, `employee.py`, `main.py`).

### What is a class?

A **class** is a blueprint for creating objects. It groups related data and behavior (functions) together.

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

An **object** is an actual instance created from that blueprint:

```python
cal = Calculator()   # cal is an object of the Calculator class
```

### What does `self` actually mean?

`self` refers to **the specific object calling the method**. Every method inside a class automatically receives the object it belongs to as its first parameter — by convention, that parameter is named `self`.

```python
class Employee:
    def employee_name(self, name):
        print("Employee name :", name)

emp = Employee()
emp.employee_name("Pranav")
```

When you call `emp.employee_name("Pranav")`, Python translates it behind the scenes into:

```python
Employee.employee_name(emp, "Pranav")
```

`emp` is automatically passed in as `self`. This is **why the method needs `self` as a parameter** — it's how the method knows *which* object's data it's working with.

### What happens if you forget `self`?

Look at the other methods in the same file — they were written **without** `self`:

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(a, b):              # missing 'self'
        print("Subtraction:", a - b)
```

Calling `cal.sub(40, 10)` will actually fail with a `TypeError`, because Python automatically passes the object as the first argument — so `a` silently becomes the object `cal`, and `b` becomes `40`, leaving no slot for `10`. This is a common beginner mistake: **every regular method inside a class needs `self` as its first parameter**, even if the method doesn't use it directly.

### Why does `self` matter? (Real-world example)

Think of a class like a **house blueprint**, and objects like **actual houses** built from it. Every house has its own address, its own furniture, its own residents — even though they were built from the same blueprint.

```python
class Employee:
    def employee_name(self, name):
        print("Employee name :", name)

emp1 = Employee()
emp2 = Employee()

emp1.employee_name("Pranav")   # self = emp1
emp2.employee_name("Veeresh")  # self = emp2
```

`self` is what lets the *same* method (`employee_name`) work correctly and independently for `emp1` and `emp2` — it's how Python tells them apart. Without `self`, every object built from the class would have no way to keep its own data separate from every other object.

### Creating and using objects

```python
from calulator import Calculator
from employee import Employee

cal = Calculator()
emp = Employee()

cal.add(10, 20)   # calls Calculator.add(cal, 10, 20) behind the scenes
cal.add(30, 40)
```

You must first **create an object** (`cal = Calculator()`) before you can call the methods defined inside that class — the object is what `self` refers to at runtime.

### Quick summary

| Term | Meaning |
|---|---|
| Class | The blueprint (e.g. `Calculator`, `Employee`) |
| Object | A real instance built from the blueprint (e.g. `cal`, `emp`) |
| `self` | Refers to the specific object calling the method — links the method to that object's data |
| Method | A function defined inside a class (usually needs `self` as its first parameter) |

## 11. Basic Git workflow (from `test.py`)

```
git clone https://github.com/pranavkumarpk01/GenAI-Jul.git   # first time only
git pull origin main                                          # first pull after clone
git pull                                                       # every time after that
```
