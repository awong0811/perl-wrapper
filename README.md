## MyModule.pm
This file is analogous to the SphereTools.pm in the SphereTools folder. You'll find two functions: one that returns a perl array of elements and one that returns a number.

The reason I did it this way is because there were two functions in SphereTools I wanted to mimic and test: apbs which returns a scalar and alanize which returns an array.

## test.pl
This file is analogous to wrapper.pl. You'll find some if else statements in there. This is because each time we call the wrapper, we usually only want to run one function. If I had to write a separate wrapper file for every function, you would probably have 50 wrapper.pl files. So instead, we are passing in arguments to activate the section of code. This way, I can have only one wrapper.pl file that calls all the 50 different functions, each in their own section.

You'll see a list of arguments in GetOptions (num and array). These are just flags that will store true or false, depending on if we send --num or --array as arguments to the script. The default is false. You should only send one of those options at a time or else you're fucked.

So each of those flags will activate the desired section of code. What each section does is essentially make a call to MyModule.pm to run the perl function. It stores the output, then prints it as a string in the "command line." You won't actually see it in your command line because this all happens behind the scenes. You have to always, always wrap the output as a string before you print and append '\n' at the end to make sure that the string is captured because stdout reads the last line. If you have an array, you may append the items with spaces as separation. This means you can print out all the items of the array in one line; you just have to parse it correctly in the python file.

## test.py
This file is analogous to NewBoxSpheres.py. You'll find the "fake" functions defined above main. These functions call the test.pl file, passing in an argument to make sure the correct perl function from the module is called. 

MAKE SURE to pass in the flag (these have -- preceding them and are the arguments for the .pl file) LAST. What I am referring to is functions like alanize. The actual perl function alanize in the SphereTools module receives four arguments. You should pass them into the wrapper before the flag. The flag should be last. This is because the .pl file will receive the flag and mark the option as true no matter the position of it in the input string, but the other arguments are position-dependent (you can see how I manually parse the arguments in wrapper.pl based on the position). Following this convention makes it easier to write the wrapper. 

## To Test the Wrapper
```bash
$ python test.py
```
This is how you run your code in python, while the code that is actually running underneath the hood is written in perl.
