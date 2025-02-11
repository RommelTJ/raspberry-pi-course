# Python 3 and the Terminal

## Install Python Modules

* You need to install some modules to use in Python.
* To view installed modules: `pip3 list`
* To search for modules: `pip3 list | grep gpio`
* To install a module: `sudo apt install python3-gpiozero` (global install)
* Or: `pip3 install gpiozero` (but you need a virtual environment)
* To remove a module: `sudo apt remove python3-gpiozero`.
* Or: `pip3 uninstall gpiozero`.

## Work with Python from the terminal

* From the terminal, you can access the Python shell with `python3`.
* To exit the Python shell, type `exit()`.
* To run a program, type `python3 s08_02_detect_movement.py`
* If you wrap code in a try-catch block, you can catch exceptions. 
  * This allows you to capture `KeyboardInterrupt` and `SystemExit` exceptions and handle them gracefully.

## Read, Write, and Manipulate Files with Python

* We made a dummy text file to read and write to.
* File I/O:
  * `r` means "read"
  * `w` means "write"
  * `w+` means "read and write"
  * `a` means "append"
* OS functions:
  * `os.path.exists(path)` returns `True` if the file exists.
  * `os.remove(path)` removes the file.
* See s10_01_read_write_files.py
