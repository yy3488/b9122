# Assignment #2 for B9122, Computing for Business Research

Out on Sep 30th, due on Tuesday Oct 8th, © 2024 Miguel Morin

This is a group assignment, with groups allocated randomly within sections.

## Exercise 1: Interest rates, recursive (35 points)

This exercise is similar to assignment 1, but now I ask that you write a recursive function and more doc-tests.

### 1.1 Recursive function (10 points)

Complete the file `compound_interest.py` to compute the interest payment on the account with a recursive function. It's similar to Assignment 1, exercise 1.1, but with a recursive function.

Submit the file on GradeScope without changing the name.

### 1.2 Differential interest rates, recursive (10 points)

Complete the file `compound_interest_differential.py` to compute the interest payment on the account, taking into account baseline and bonus interest rates. It's similar to Assignment 1, exercise 1.2, but with a recursive function.

Submit the file on GradeScope without changing the name.

### 1.3 Diferential interest rates (5 points)

Complete the file `compound_interest_robust.py` to take into account all the possible edge and corner cases you can think of. Write these corner cases as doc-tests, then implement the code that handles those edge cases.

Submit the file on GradeScope without changing the name.

## Exercise 2: System administration (30 points)

You installed my attendance software by pull the source code as text files; installing software this way is called "**from source**." When you installed Anaconda or PyCharm, you used an installer (a file with extension `.dmg` on `macOS` and `.exe` on `Windows`), which is a binary file (not a text file); installing software this way is called "**from binary**." Although it may have been frustrating, this question will show you some advantages of installing software this way.

Imagine that you attended a presentation and were given the video file with the recording. The file is 2 GB and contains nothing but slides. Unfortunately, the presenter did not give you the slides. You want to extract the slides as a PDF file so you can add your own notes, and also to save space (the PDF file could be 2 MB, instead of 2 GB for the video file).

This GitHub repository contains a Python tool to do that: [https://github.com/mm3509/video2pdf](https://github.com/mm3509/video2pdf) (adapted from the original at: [https://github.com/kaushikj/video2pdf](https://github.com/kaushikj/video2pdf) ).

### 2.1 Installation (10 points)

In a **new** shell, install this tool with `git` and `pip`, just like you did with my attendance code.

Note: if your version of Python is 3.12.5, you may find a `ModuleNotFoundError` about `distutils`. Please upgrade to Python 3.12.6.

Save the output from the shell as a text file and submit it on GradeScope as `system1.txt`.

### 2.2 Usage: presentation only (10 points)

On Canvas and Echo360, download the slides from the first lecture in the morning section, in the morning section, low-quality version. It should be 150.9 MB.

Use the installation from the previous step and run the tool on this file. Your PDF should contain N pages (about one per slide). (TBA: I'll add the video files and the slide number if this question stays.)

Submit that PDF file on GradeScope as `system2.pdf`.

### 2.3 Usage: presentation + camera (10 points)

Sometimes, a video file has both the slides and a camera recording. In this case, the algorithm needs adjustment in order to detect the change in slides that is not from the change in the person's face.

Download the recording from another lecture where the presenter has both their slides and a small window for the presenter talking, or the presenter alternates between sharing the slides as a presentation and the in-room camera.

Find where in the source code you can adjust this setting. Run the tool to extract the slides into a PDF file. Check the PDF file to confirm that you are not missing any slides.

Submit that PDF file on GradeScope as `system3.pdf`.

### 2.4 Advantages and disadvantages (bonus, 5 points)

What advantages do you see in installing software from source as opposed to binary? What disadvantages do you see?

## Exercise 3: OCR and debugging (40 points)

### 3.1 Debugging (20 points)

The file `knn.py` implements the OCR system we mentioned in lecture 1. Install the required dependencies and check that you can run the code `knn.py`. The function `kNN()` in the general case is for your reference of how to implement k-Nearest Neighbors in the general case and you can ignore it.

This Python file has a bug. Find and correct it.

Note: this file has no doc-tests, so I give no indication of where the bug is.

(Hint: visually compare an image from the test data to its nearest neighbor from the training data.)

Submit the file on GradeScope without changing the name.

### 3.2 Accuracy (20 points)

The file `knn_accuracy.py` imports the file above (whether or not you found the bug). Complete the function in the file to compute the accuracy of 1-nearest neighbor as an OCR system.

That is, run the algorithm on images from the test data (`test_x`), compare the algorithm's prediction to the true value (`test_y`), and report the percentage of images where the algorithm found the right answer.

Submit the file on GradeScope without changing the name.

### 3.3 Speed (5 points)

How long did your code take to compute the accuracy? Why do you think the Python code took that amount of time?

Submit your answer on GradeScope as a text file with `knn3.txt`.

### 3.4 Bonus (5 points9

Inspect some of the images that the algorithm got wrong. Why did that happen? How could another algorithm solve it?

Submit your answer on GradeScope as a text file with `knn4.txt`.
