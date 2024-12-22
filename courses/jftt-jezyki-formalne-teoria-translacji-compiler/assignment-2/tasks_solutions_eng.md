# Tasks
## Exercise 1
Write program in `Flex` which
1. Reads any text file
2. Deletes all whitespaces in the beginning and in the end of a line
3. Replaces all occurrences of space and tab in a row to exactly one `space`
4. Deletes empty lines
5. Appends to the end of the file amount of lines and words in the file. These should be separated by white space.
## Exercise 2
Write program in `Flex` which removes all comments in `python` source codes
## Exercise 3
Write program in `Flex`, which removes all comments in programs written in `C++` Language.
After executing the program with `--leave-docs` it shouldn't remove documentation comments.
### Note: 
`Documentation comments` are the ones which start on `/**` or `/*!` or `///` or `//!`.
## Exercise 4
By using `Flex`, implement simple postfix calculator (reverse polish notation) to integers. Calculator should implement operations like: 
1. \+ (addition) 
2. \- (substraction)
3. \* (multiplication)
4. / (integer division)
5. ^ (exponentation)
6. % (modulo)  

`Input`: Expression should be written in one line.   
`Output`: Program should display evaluated value of expression or communicate about exception.  
Example:
```
./Calculator
 2 3+4*
= 20
1 2 3 4 + * -
= -13
-1 2 -3 4 + * -
= -3
8 -7 6 -5 4 * -3 % / - +
= 4
2 3 2 ^ ^
= 512
2 3+*
Error: Expected more arguments
2 3 4 +
Error: Expected more operators
2.4 3+
Error: Wrong token "."
```