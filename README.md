# b9122

Repository for class Computing for Business Research

## How to mark attendance

After following the steps below to install, you can mark attendance in 4 ways, listed below by order of preference:

1. start a shell (`Terminal.app` on macOS, `git bash` on Windows) and run this command:

```bash
cd; cd b9122; git pull; python mark_attendance.py
```

2. start a Jupyter notebook **in this directory** `cd; cd b9122; jupyter notebook`, open the notebook `mark_attendance.ipynb`, and run the first cell

3. start a Python interpreter, or use a new cell in your Jupyter notebook, copy-paste the code below, and run it. You may need to change the folder in the fourth line to where you installed my code. Also, this option will not update your copy of my code to the latest version.

```python
import os

# Change this to your own b9122 folder.
os.chdir(os.path.expanduser("~/b9122"))

from b9122 import b9112
b9122.mark_attendance()
```

## Install software to mark attendance

You only need to follow these steps once (or multiple times, if you choose to install manually instead of git). Each step ends with a validation for you to confirm that it succeeded

### Install a bash shell

#### On Windows

Download and install Git for Windows from: [www.gitforwindows.org](www.gitforwindows.org). Say OK to all the default settings. Add the program to the task bar and you should see this symbol:

<img src="https://avatars.githubusercontent.com/u/4571183?s=200&amp;v=4" width="100" height="100" alt="@git-for-windows">

#### On MacOS

Search for `Terminal.app` on Spotlight. Launch it. Go to the Dock, right-click on the Terminal application, click on "Options" and then on "Keep in Dock", so it's always there. You should see a program running with this symbol:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Terminalicon2.png/120px-Terminalicon2.png">

#### validation

**Validation***: Copy-paste this code and press ENTER:

``` bash
echo $HOME
```

You succeeded if you see the path to the home folder of your computer, e.g. `/Users/mm3509` on macOS or `/c/Users/mm3509` on Windows.

### Clone this repository

#### with git and command shell

In the shell you opened above, copy-paste this code:

``` bash
cd; git clone https://github.com/mm3509/b9122
```

You should see something like this:

``` bash
Cloning into 'b9122'...
remote: Enumerating objects: 64, done.
remote: Counting objects: 100% (64/64), done.
remote: Compressing objects: 100% (41/41), done.
remote: Total 64 (delta 34), reused 46 (delta 19), pack-reused 0 (from 0)
Receiving objects: 100% (64/64), 9.39 KiB | 1.88 MiB/s, done.
Resolving deltas: 100% (34/34), done.
```

#### manually

If you get an error such as `Please make sure you have the correct access rights and the repository exists`, please come see me during Office Hours so I debug and fix this. In the meantime, you can download the software manually:

- visit this link: [https://github.com/mm3509/b9122](https://github.com/mm3509/b9122)

- search for the green button at the top right that says `Code`

- click on the down arrow

- click on Download ZIP

- look for the ZIP file in your Downloads folder

- extract to your home folder **without** the path `b9122` (otherwise, you'll have a nested extraction)

If you get a nested folder, e.g. `b9122/b9122`, please move the nested folder up one level, so there's only one `b9122` in the path.

#### validation

Copy-paste this code in a shell:

``` bash
cd; cd b9122; ls mark*
```

You succeeded if you see this:

``` bash
mark_attendance.ipynb mark_attendance.py
```

### Connect the shell to your installation of Python

### on macOS

Normally, you don't need to do anything. Python is already installed on macOS, and if you installed Anaconda Python properly, every new shell starts in an Anaconda environment.

### on Windows

1. Make sure you installed Anaconda Python from [here](https://www.anaconda.com/download/success).

2. Run a command prompt shell: in the search box, type `cmd` and press ENTER (or search for CMD, and click on the black icon, not the blue icon which is the Windows Power Shell, nor the multi-colored icon, which is the Git Bash shell)

3. Type this command (and notice it's **conda**, not **anaconda**):

``` bash
where conda
```

You should see a result like:

``` bash
C:\Users\mm3509\AppData\Local\anaconda3\condabin\conda.bat
```

Note the path until `condabin`, change the initial `C:\` to `/c/`, and change all backslashes to forward slashes: `\` -> `/`, so it becomes:

``` bash
/c/Users/mm3509/AppData/Local/anaconda3
```

And add this text to the end of the path: `/etc/profile.d/conda.sh`, for example:

``` bash
/c/Users/mm3509/AppData/Local/anaconda3/etc/profile.d/conda.sh
```

4. In a **Git Bash shell** (not a CMD shell, nor a Power Shell), edit this code so the first line uses the path from the step before, and press ENTER:

``` bash
echo ". /c/Users/mm3509/AppData/Local/anaconda3/etc/profile.d/conda.sh" >> ~/.bash_profile
echo "conda activate" >> ~/.bash_profile
echo "alias python3=python"
```

## Notes for Windows users

1. If the shell seems to do nothing, please close it and run it again, or ask for my help.

1. Whenever you see a command like `python` or `python3` alone in my material, you have to add ` -i` to the command to run an interpreter. Otherwise, Python is running but you don't see it, and it seems like nothing happens. Close the window and start a new one.

