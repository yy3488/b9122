# b9122

Repository for class Computing for Business Research

## How to mark attendance

After following the steps below to install, you can mark attendance in 3 ways, listed below by order of preference:

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

## Update software to mark attendance (recurring)

I may update the software to fix bugs or to incorporate your feedback, so you'll have to update it as well.

After following the steps below to install the software, you can update it by starting a shell (Terminal.app on macOS or Git Bash on Windows), typing this code, and running:

``` bash
cd; cd b9122; git pull; python3 mark_attendance.py
```

or simply calling the "alias" defined in the installation:

``` bash
miguel
```

## Install software to mark attendance (one-off)

You only need to follow these steps once (or multiple times, if you choose to install manually instead of git). Each step ends with a validation for you to confirm that it succeeded

### Install a bash shell

#### On Windows

Download and install Git for Windows from: [www.gitforwindows.org](www.gitforwindows.org). Say OK to all the default settings. Add the program to the task bar and you should see this symbol:

<img src="https://avatars.githubusercontent.com/u/4571183?s=200&amp;v=4" width="100" height="100" alt="@git-for-windows">

#### On MacOS

1. Search for `Terminal.app` on Spotlight. Launch it. Go to the Dock, right-click on the Terminal application, click on "Options" and then on "Keep in Dock", so it's always there. You should see a program running with this symbol:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Terminalicon2.png/120px-Terminalicon2.png">

#### Validation

Copy-paste this code and press ENTER:

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

If you get an error that the repository already exists, please run this code instead:

```
if [ -d ~/b9122 ]; then mv ~/b9122 ~/b9122_backup; fi
cd; git clone https://github.com/mm3509/b9122
if [ -d ~/b9122_backup ]; then mv ~/b9122_backup/\.*.txt ~/b9122/; rm -rf b9122_backup; fi
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

#### Install manually

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

### On macOS

Normally, you don't need to do anything. Python is already installed on macOS, and if you installed Anaconda Python properly, every new shell starts in an Anaconda environment.

### On Windows

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
echo 'alias python3="python"' >> ~/.bash_profile
```

Note that the last line creates an alias to call `python` whenever you type `python3`. This is for compatibility with my material (because some computers have both `python` for Python 2 and `python3` for Python 3).

5. For these changes to take effect, close your shell and open a new one.

#### Errors

If Windows open the Microsoft Store when you run `python` in a shell, please remove the execution aliases. Go to Settings > Apps and features > App Execution Aliases and turn off the items called "App Installer" that start with `python` and end with `.exe`. See [this thread](https://superuser.com/questions/1437590/typing-python-on-windows-10-version-1903-command-prompt-opens-microsoft-stor/1461471#1461471) for details.

<img src="https://i.sstatic.net/cbdFj.png">

### Validation

You succeeded if you can get the Python version from a shell (Terminal.app or Git Bash):

``` bash
python3 --version
```

You should see something like:

``` bash
Python 3.12.4
```

## Install the requirements for this repository

1. Open a new shell (Terminal.app or Git Bash)

2. Copy-paste this code and press ENTER:

``` bash
python3 -m pip install -r requirements.txt
```

You should see something like:

``` bash
Requirement already satisfied: requests in ...
```

### Validation

You succeeded if you can type this in a shell (Terminal.app or Git Bash) and press ENTER:

``` bash
cd; cd b9122; python3 mark_attendance.py
```

and see this result:

``` bash
Software version: September 24th, 2024
...
```

## Define a shortcut (alias) to run the code (optional)

### On macOS

Start a new shell. We'll use the Nano text editor, which can be daunting at first, to edit a system file that macOS normally doesn't let us access:

``` bash
sudo nano ~/.zshrc
```

Enter your password

Use the down arrow key to get to the bottom of the file, then type this code AS-IS:

``` bash
alias miguel="cd; cd b9122; python3 mark_attendance.py"
```

Hit Control-O to save the file, then ENTER to validate that save. Hit Control-X to exit the editor.

### On Windows

Start a new shell, copy-paste this code, and press ENTER (it may ask for your password):

```
echo 'alias miguel="cd; cd b9122; python3 mark_attendance.py"' >> ~/.bash_profile
```

### Validation

Now you can mark attendance by simply running `miguel` in a shell.

Start a **new shell**, copy-paste this code, and type ENTER:

```
miguel
```

You succeeded if you see this result:

``` bash
Software version: September 24th, 2024
...
```

## Notes for Windows users

1. If the shell seems to do nothing, please close it and run it again, or ask for my help.

1. Whenever you see a command like `python` or `python3` alone in my material, you have to add ` -i` to the command to run an interpreter. Otherwise, Python is running but you don't see it, and it seems like nothing happens. Close the window and start a new one.

