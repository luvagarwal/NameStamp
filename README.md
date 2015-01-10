USAGE
--------
To write your nick on the github contribution dashboard.

![](img.png?raw=True)

How To?
--------
  1. Clone this repo.
  2. Add a new repository to your github (will be used to push the false commits) and initialize that.
  3. Run write.py in the NameStamp repo.

To darken the name, run script multiple times.

Undo the state of contribution board
-------------------------------------
Simply delete the new repo that you made for the false commits.

Any Changes?
---------------
Currently only upper case letters are supported. So it automatically converts your nick to uppercase string.
To support other characters, they have to be added to the alphabets dictionary in bitmap.py and remove the autoconversion of nick to uppercase string.
Pull requests are welcome :).

For any issues mail me at agarwal.iiit@gmail.com
