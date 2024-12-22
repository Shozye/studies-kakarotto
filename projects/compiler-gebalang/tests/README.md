# Description
Tester is an application that runs compiler on several testfiles and:
- Provides user with passed testcases statistics
- Creates file with differences between expected and actual testcase if test did not passed
- Provides statistics about speed and code length of generated assembler in testcases
- Compatible with python sly and bison
# Usage
```
python tester.py -p interpreter.py
```
```
python tester.py ./interpreter
```
# Output
```
tests_errors: +++++++++
tests_variables: +++-++
tests_procedures: +++++
tests_loop: ++-++
TESTS FAILED:
tests/tests_variables/add.imp - Creation of variables and adding them together
tests/tests_loop/while2.imp - Program searches square root of 10000 by checking from 1 to 10000 in loop 
Errors exported to: errors.log
PASS RATIO: 23/25 = 92%
Summarized cost: 91280
Sum line length: 352
```
