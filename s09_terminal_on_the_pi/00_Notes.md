# Use the Terminal on Your Raspberry Pi

## Navigation and File System

* You open the terminal by clicking the button or connecting via SSH.
* `pwd` prints the current working directory.
* `ls` lists the contents of the current directory. `ls -a` lists all files, including hidden files.
* `cd` changes the current working directory.
* You can use tab for autocomplete.

## Edit Files from the Terminal with Vi

* The course uses Nano but I use Vi
* To make a new file
  * `vi filename`
  * Type `i` to enter insert mode.
  * Type your content.
  * Type `:wq` to save and exit.
* Line navigation
  * Arrow keys to move around, or `h` and `l` to move left and right and `j` and `k` to move up and down.
  * `0` to move to the beginning of the line.
  * `$` to move to the end of the line.
  * `^` to jump to the first non-blank character of the line.
* Word navigation
  * `w` to move to the beginning of the next word.
  * `b` to move to the beginning of the previous word.
  * `e` to move to the end of the next word.
* Screen navigation
  * `Ctrl + f` to move forward one screen.
  * `Ctrl + b` to move backward one screen.
  * `G` to move to the bottom of the file.
  * `gg` to move to the top of the file.
  * `:number` to move to the specified line number.
* Quick jumps
  * `%` jump to matching parenthesis.
  * `H` jump to the top of the screen.
  * `M` jump to the middle of the screen.
  * `L` jump to the bottom of the screen.
* To exit between modes, type `Esc`.

## Create, Remove, and Manipulate Files

* Meh.

## Install and Update Software

## A Few More Terminal Commands to Gain More Control Over Your Pi

