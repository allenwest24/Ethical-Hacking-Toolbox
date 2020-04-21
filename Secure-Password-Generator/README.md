# Secure-Password-Generator
This password generator is designed to generate a secure, memorable password using the XKCD method. 

## Features
-w (num) will allow you to set the number of words pulled from the given dictionary. Default is 4.
-c (num) will allow you to randomly capitalize the given number of letters within the word.
-n (num) will allow you to randomly insert the given amount of random numbers into the password.
-s (num) will allow you to randomly insert the given amount of random symbols into the password.

## Usage and Examples
- python password-gen.py
Result: babytacovaccuumtree

- python password-gen.py -w 3 -c 3 -n 5 -s 2
Result: b1Abyt%a3cOv8ac&cUu7m5


