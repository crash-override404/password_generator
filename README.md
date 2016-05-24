## Password generator

This generator allows to create password(s) using phrase, salt and password length.
Password is generated from matrix, which contains random generated dictionary.

### How it works

Generate password is easy. Just call password_generator.py from command line with some arguments:
* phrase - some word, could be anything, like your girlfriend's name, site name for which you are generating password - whatever
* salt - some random value - again, it can be anything - PIN-like value eg. 1231, dog's name, twenty 'A' letters
* password length - remember, length of your password is the key to prevent it from bruteforce attack with tools like Hydra or John The Ripper - 30 and more characters is quite good idea here


Let's see some examples:

```
$ ./password_generator.py facebook mysalt12 32
P6vCahI3P6vCahI3P6vCahI3P6vCahI

$ ./password_generator.py mypasswordtoGMAIL mysalt12 40
ve]zo8PtrGMZmZoFnYvgD8n8PlvuoDIpha2ywqn

```

*Important* - you will get exactly *THE SAME PASSWORD* from each combination of phrase, salt and length using *THE SAME MATRIX* 
If you'll change matrix - you won't be able to get the same passwords anymore.

Of course, before you'll start to use this generator, you can generate your own matrix (see matrix_generator.py). Just run it and change content of matrix.py file with your result. Or create your own matrix by hand, if you want :)



### Notice

I've used only diggits, upper- and lowercase letters for phrase and salt. You can modify this behaviour if you want.
