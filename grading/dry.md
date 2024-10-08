# Guidance / grading on DRY / Don't Repeat Yourself

This document explains our human judgment on what constitutes "DRY" code.

As a rule-of-thumb, if you ever find yourself copy-pasting code, consider "refactoring" that piece of code you were about to copy into:

- a variable that you use multiple times

- a function that you can call

- a module that you can import

## example from math

The concept of "refactoring" in programming is similar to "factoring" in math.

This expression is called "distributed":

```
a + a + a + a + a
```

and has the same value as this expression, which is "factored":

```
5 * a
```

but the latter is shorter, simpler, easier to read, and less likely to have bugs.

## simple rules-of-thumb

### Use augmented assignment operators

When peforming arithmetic operations to update a variable, use the operators `+=`, `-=` and `*=`. These are called **augmented assignment operators** because they combine an operation with an assignment.

That is, the following four arithmetic operations:

```
a = a + 1
b = b - 2
c = c * 3
d = d / 4
```

are the same as, and should be replaced by:

```
a += 1
b -= 2
c *= 3
d /= 4
```

This saves about one third of characters and reading time.

### Use default arguments

To get a range, for example from `0` to `30`, use the default argument for the start, which is zero.

That is, instead of writing:

```
range(0, 30)
```

you should write:

```
range(30)
```

## examples from assignment 1

### exercise 1.1

Here is an example of WET code:

```
interest = 0
days_passed = 0
if len(transactions) > 0:
    for i in transactions:
        interest = interest + ((1 + rate) ** (1 / 365)) ** (i[0] - days_passed) * balance - balance
        balance = balance + i[1]
        days_passed = i[0]
    interest += ((1 + rate) ** (1 / 365)) ** (days_in_month - days_passed) * balance - balance
elif len(transactions) == 0:
    interest += ((1 + rate) ** (1 / 365)) ** days_in_month * balance - balance
```

In the case of no transactions, `days_passed = 0`, so the last line and the third-to-last line are the same and should be "refactored", which eliminates three lines of code (or 30% of the original lines):

```
interest = 0
days_passed = 0
for i in transactions:
    interest = interest + ((1 + rate) ** (1 / 365)) ** (i[0] - days_passed) * balance - balance
    balance = balance + i[1]
    days_passed = i[0]
interest += ((1 + rate) ** (1 / 365)) ** (days_in_month - days_passed) * balance - balance
```

### exercise 1.2

Here is an example of WET code: 

```
def calculate_interest_differential(balance,
                                    baseline_rate,
                                    bonus_rate,
                                    transactions):
    """ Doc-string ommitted for clarity. """
    true_rate = (1 + bonus_rate) ** (1 / 365) - 1
    merged_dict = {}
    
    for day, amount in transactions:
        if day in merged_dict:
            merged_dict[day] += amount
        else:
            merged_dict[day] = amount
        if amount < 0:
            true_rate = (1 + baseline_rate) ** (1 / 365) - 1
    
    interest_compounded = 0
    
    for interest_day in range(30):
        balance += merged_dict.get(interest_day, 0) 
        interest_compounded += balance * true_rate
        balance += balance * true_rate
    round(interest_compounded, 2)
```

Notice that, if the baseline rate applies, the formula for it is inside two indentations. If we have to change the number of days in a year, for example because of a leap year (366), or to calendar days (360, twelve times 30), it will be easy to introduce a bug by changing it only at the top.

Instead, DRY code uses the function defined in the above exercise. A Python file is a module and you can import it!


```
from compound_interest_solution_DRY import calculate_interest

def calculate_interest_differential(balance,
                                    baseline_rate,
                                    bonus_rate,
                                    transactions):
    """ Doc-string ommitted for clarity. """
    rate = bonus_rate
    for _, amount in transactions:
        if amount < 0:
            rate = baseline_rate
            break

    return calculate_interest(balance, rate, transactions)
```