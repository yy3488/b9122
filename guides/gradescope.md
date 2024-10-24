# Gradescope

We use GradeScope for submissions.

## Submission checklist

Please ensure that you run these checks locally, on your computer, before uploading to Gradescope.

### Delivery: Your file is valid code

Make sure that your file is valid Python. For example, for a file called `exercise1.py`, run this in a shell:

``` bash
python exercise1.py
```

And solve any `SyntaxError` or `IndentationError` that you see.

Your Python file should follow this structure (without my comments):

```python
# Imports at the top
import sklearn


# Global variables next, uppercase
NEIGHBORS_KNN = 2


# Functions come next.
def square(num):
    """
    This is a doc-string. It's the triple-quoted string right after a function
    definition. It contains doc-tests. For now, you don't to write anything here
    other than doc-tests.
    
    These are doc-tests, starting with triple angled brackets and a space.
    The line after the triple-quoted bracket is the expected result.
    Corner cases should use the syntax below for the "traceback" of the error.
    >>> square(2)
    4
    >>> square("2")
    Traceback (most recent call last):
    ...
    ValueError: argument must be a number
    """
    
    if not isinstance(width, (int, float)):
        raise ValueError("argument must be a number")
        
    return num ** 2
    

# Classes come next, if any
class MyClass(object):
    pass


# A main function comes next, if any.
def main():
    pass


# Finally, if you want to run code when the file is run but not when it's imported,
# use the "dunder" variable `__name__`, which is then equal to "__main__":
if __name__ == "__main__":
    main()
```

### Doc-tests: Your file passes your doc-tests

Make sure that your file passes your doc-tests. For example, for a file called `exercise1.py`, you would run this:

``` bash
python -m doctest exercise1.py
```

If you see nothing, your file either has no doc-tests or they all pass. If you want to see the full output of the test, add the `-v` switch (v for "verbose"):

``` bash
python -m doctest -v exercise1.py
```


## FAQ

### How to create an account

Click on "Gradescope" on the left bar on Canvas and use your Columbia email.

### How to upload a submission

[Here](https://courseworks2.columbia.edu/files/21823761/download?download_frd=1) is a screencast from Canvas on how to upload a submission.

### Autograder is unresponsive, what do I do?

Gradescope seems to have a bug and shows a page saying `The autograder hasn't finished running yet.` well after the 10 minute timeout:

![](../images/Gradescope_unresponsive.png)

In this case, please submit again and Gradescope will try to grade again.

### How do I upload a PDF file?

Click "Submit" or "Resubmit", then just drag-and-drop a PDF file onto the window.
