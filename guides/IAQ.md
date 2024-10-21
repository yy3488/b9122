# Infrequently Asked Questions

This document contains answers to questions infrequently asked, which I will answer here to keep the precious lecture time focused on the material.

## Lecture 6, morning

### Can I run code in PyCharm like I would in a Jupyter Notebook?

Yes, you can. Select the code you want to run, right-click on it, then choose `Execute Cell in Console`.

You will then see an interface similar to Jupyter.

## I don't see `Inspect Element` in Safari

You need to enable Developer tools to see the page source of a web page (detailed steps [here](https://www.howtogeek.com/721416/how-to-turn-on-the-develop-menu-in-safari-on-mac/)).

## Lecture 6, afternoon

### How does SciKit-Learn compare to the built-in Statistics module?

From the [documentation](https://docs.python.org/3/library/statistics.html):

> The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.

For example, you can compute means, standard deviations, and even a linear regression using the `statistics` module.

For more advanced models like logistic regression and k-Nearest Neighbors, we need SciKit-Learn. So we just use SciKit-Learn.

### Why is the identity matrix called `eye`?

In math, the identity matrix uses the single letter "I" and the "spelling name" for it is "eye" or "aye". For more details, or other spelling names, read [this thread](https://math.stackexchange.com/questions/3028394/what-is-the-motivation-behind-naming-identity-matrix-as-eye).

### Why is it called "saving to disk"?

Back in the day, hard drives were magnetic disks spinning around. Even though now our storage today is not on disks (we have "solid state drives" and "flash storage"), the expression stayed. The reason is similar to why the "save" icon is a [floppy disk](https://en.wikipedia.org/wiki/Diskette), or "diskette", even though we haven't used them for 20 years.
