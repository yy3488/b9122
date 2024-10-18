# Midterm exam (in-person, for morning section)

For all these questions:
- complete the relevant Python function and submit it on Gradescope without changing the name of the file or of the functions;
- you can import other modules, including those you wrote yourself (to be DRY);
- all your functions should have doc-tests and apply defensive programming.

## Python string manipulation

This function takes a string and converts it to title case. Title case means that the first letter is uppercase and every letter at the start of a word is upper case (unless they are a "stopword", which in this case will only be three of them: "a", "the", "of").

## debugging: Python dictionary manipulation

CBS has two email adddresses for the same person. These different usernames are called "aliases". For example, for me they could be:

- UNI: mm3509@columbia.edu
- GSB, with graduation year: MMorin26@gsb.columbia.edu

I will give you a dictionary with details on students' grades. The keys of the dictionary are the UNIs in lowercase. The value of the dictionary is **another** dictionary with the following keys:

- `"gsb"`: the CBS username with graduation year
- `"grade"`: the grade

Write a function that takes as arguments an email and this dictionary, and returns the grade. You will need the function `.lower()`, which converts a string to lower case.

This function does this search, but it has a bug. Find it and fix it:

```
    def get_person(uni, grades):
        if not (isinstance(uni, str) and isinstance(grades, dict)):
            raise ValueError()

        if "" == uni:
            return None

        uni = uni.lower()
        if uni in grades
            return grades[uni]["grade"]

        for uni in grades
            person = self.grades[uni]
            if "gsb" in person and person["person"].lower() == uni:
                return grades[uni]["grade"]

        raise IncorrectSubmissionException("UNI not in JSON file: " + uni)
```

## speed: prime numbers

This function takes a positive integer as argument and returns all prime numbers until it.

Note: if your function is slow, read about the ["Sieve of Erathostenes"](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

## Integral calculation

A Riemann integral is the successive approximation of the integral of a function, as in this image:

<img src="https://upload.wikimedia.org/wikipedia/commons/2/28/Riemann_integral_regular.gif" />

Complete the function in TBA. For clarity, I will refer to this as "your Python function", and to the function whose integral you'll compute as the "my analytic function". My analytic function will be an argument to your Python function (indeed, Python can store functions into variables and you can pass them around; it's a programming paradigm called "functions as first-class citizens").

It computes an iteration in this approximation of the integral of a function. Your function takes as arguments:

- my analytic function

- a start for the range (interval) where to compute the integral

- an end for the range (interval) where to compute the integral

- a step, or width of the bars in the image

Your Python function should use the value of my analytic function at the midpoint; for example, if the start is 0, then end is 0, and the step is 0.2, you should use the values of my analytic function at 0.1, 0.3, 0.5, 0.7, and 0.9.

Your Python function should return the approximate value of the integral of my analytic function over the given range and with the given step.

## reading and parsing a CSV file

A CSV file (Comma-Separated Values) is a common format for data storage. It is similar to Excel's XLS, but it only stores data or values (no formulas). It has a delimiter, most commonly a comma, to separate columns; and the delimiter to separate rows is usually a newline (the value in Python is `"\n"`).

For example, a CSV file with income by county in the US would look like this:

```
county,state,income
Kings,NY,1234
Queens,NY,6789
```

### imperative function

Write a function in imperative style that takes as input a string with a line in the CSV file, and returns a list with the value of each cell, for example on the first line it would return:

```
["county", "state", "income"]
```

### recursive function

Sometimes, the value of a cell has the delimiter itself, for example "Washington, D.C." In this case, the CSV format stores it with quotes around the name, for example:

```
county,state,income
"Washington, D.C.",DC,1234
```

Complete the recursive function that handles this case and removes the quotes. For the second line in the above example, it should return:

```
["Washington, D.C.", "DC" , "1234"]
```

### function to read from a file

Complete the function that takes as argument a filepath and returns a list of lists with the contents of the file.

The function should call the recursive function. (The recursive function is then a "helper" function to help the main function, called a "wrapper" that wraps around the helper function.)


## other ideas

I can add these ideas to make for 3 hours of an exam or I can leave them for the final

- web scraping (complete the web scraping to get data from a website)
- logistic regression
- numpy manipulation
- kNN classification
