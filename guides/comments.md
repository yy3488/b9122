# Guidance on comments

Comments are a cost: they are not executed and can become out of date.

## academia versus industry

I know that in other classes, you are required to comment every line of your
code. That may be the case in academia, but it's not the case in industry, and
so it's not in this class either.

## Google Python Style Guide

Please read this section of the [Google style
guide](https://google.github.io/styleguide/pyguide.html#385-block-and-inline-comments):
comments are only allowed in doc-strings (the lines starting with `"""` after a
function definition) and in tricky parts of the code:

One relevant example from the Style Guide is this quote:

> Never describe the code. Assume the person reading the
> code knows Python (though not what you’re trying to do)
> better than you do.

Also, please note that when I add comments in the code, I do so to
help you learn.  Please tell me if you would prefer that I don't write
any comments so as not to confuse you.

Over the term, you'll develop a better sense of when the benefit of a
comment exceeds this cost.

## Examples

This section contains examples from the [StackOverflow best practices on comments](https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/), appçlied to Python.

They are examples of comments you can safely
remove.

### redundant comments

Please delete all redundant comments, which say exactly the same as
your code, such as this example:

```python
# Iterate through the dictionary.
for key in dictionary:
   ...
```

### renaming variables to avoid comments

Consider renaming your variables to make them more explanatory
and delete comments. This is an example of a bad comment:

```python
def rectifier(some_list):
    # Largest value candidate.
    b = 0
    for n in some_list:
        if n > b:
            b = n
    return b
```

By changing the variable name, we don't need a comment at all:

```python
def rectifier(some_list):
    largest_so_far = 0
    for n in some_list:
        if n > largest_so_far:
            largest_so_far = n
    return largest_so_far
```
