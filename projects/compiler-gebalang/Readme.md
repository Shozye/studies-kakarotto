# Introduction
Compiler of Gebalang written by Mateusz Pelechaty  
Gebalang is programming language invented for the purpose of `Formal Languages and Translation Theory` course conducted at Wroclaw University of Science and Technology.
Lecture is taught by `dr. Maciej Gębala`. Compiler provides basic optimisation.
For information about language see bottom of this file.

## Compilation
Compile using
```
python3 run.py <input_path> <compiled_path>
```
## Requirements
Python >= 3.9 is needed  

See dependencies in ```requirements.txt```

It is expected that user will create virtual environment and install packages through
```
python3 -m pip install -r requirements.txt
```
## Files description

- `requirements.txt` contains needed libraries
- `run.py` file that executes compiler
- `src` directory with source code of compiler
    - `gebalang` package that creates TAC from Gebalang
    - `control_flow_graph` package that creates Control Flow Graph from TAC
    - `tac_validator` package that validates TAC
    - `standard_library` package that contains assembler functions
    - `translator` package that translates TAC CFG to Assembler CFG
    - `merger` package that merges Assembler CFG to one file assembler
    - `common` package with common classes between packages
    - `assembler_optimiser` package with optimising classes for assembly cfg
    - `cfg_optimiser` package with optimising classes for tac cfg
    - `main.py` library main method

## Gebalang
Sample Gebalang file looks like this:
```
[ program to calculate gcd of 4 numbers ]
PROCEDURE swap(a,b) IS
VAR c
BEGIN
  c:=a;
  a:=b;
  b:=c;
END

PROCEDURE gcd(a,b,c) IS
VAR x,y
BEGIN
  x:=a;
  y:=b;
  WHILE y!=0 DO
    IF x>=y THEN 
      x:=x-y;
    ELSE 
      swap(x,y);
    ENDIF
  ENDWHILE
  c:=x;
END

PROGRAM IS
VAR a,b,c,d,x,y,z
BEGIN
  READ a;
  READ b;
  READ c;
  READ d;
  gcd(a,b,x);
  gcd(c,d,y);
  gcd(x,y,z);
  WRITE z;
END
```
Gebalang supports following grammar:

|               |                                                                       |
|---------------|-----------------------------------------------------------------------|
| program_all   | procedures main                                                       |
| procedures    | procedures PROCEDURE proc_head IS VAR declarations BEGIN commands END |
|               | procedures PROCEDURE proc_head IS BEGNI commands END                  |
|               | %empty                                                                |
| main          | PROGRAM IS VAR declarations BEGIN commands END                        |
|               | PROGRAM IS BEGIN commands END                                         |
| commands      | commands command                                                      |
|               | command                                                               |
| command       | identifier := expression;                                             |
|               | IF condition THEN commands ELSE commands ENDIF                        |
|               | IF condition THEN commands ENDIF                                      |
|               | WHILE condition DO commands ENDWHILE                                  |
|               | REPEAT commands UNTIL condition;                                      |
|               | proc_head;                                                            |
|               | READ identifier;                                                      |
|               | WRITE value;                                                          |
| proc_head     | identifier ( declarations )                                           |
| declarations  | declarations, identifier                                              |
|               | identifier                                                            |
| expression    | value                                                                 |
|               | value + value                                                         |
|               | value - value                                                         |
|               | value * value                                                         |
|               | value / value                                                         |
|               | value % value                                                         |
| condition     | value = value                                                         |
|               | value != value                                                        |
|               | value > value                                                         |
|               | value < value                                                         |
|               | value >= value                                                        |
|               | value <= value                                                        |
| value         | num                                                                   |
|               | identifier                                                            |




## Virtual Machine
Virtual machine was created by `dr. Maciej Gębala` and can parse following assembler directives:

| Directive | Interpretation                                          | Time |
|-----------|---------------------------------------------------------|------|
| GET i     | gets number from input and saves it in p_i and k <- k+1 | 100  |
| PUT i     | Prints p_i and k <- k+1                                 | 100  |
| LOAD i    | p_0 <- p_i and k <- k+1                                 | 10   |
| STORE i   | p_i <- p_0 and k <- k+1                                 | 10   |
| LOADI i   | p_0 <- p_{p_i} and k <- k+1                             | 10   |
| STOREI i  | p_{p_i} <- p_0 and k <- k+1                             | 10   |
| ADD i     | p_0 <- p_0 + p_i and k <- k+1                           | 10   |
| SUB i     | p_0 <- p_0 - p_i and k <- k+1                           | 10   |
| ADDI i    | p_0 <- p_0 + p_{p_i} and k <- k+1                       | 10   |
| SUBI i    | p_0 <- p_0 - p_{p_i} and k <- k+1                       | 10   |
| SET x     | p_0 <- x  and k <- k+1                                  | 10   |
| HALF      | p_0 <- floor{p_0 / 2} and k <- k+1                      | 5    |
| JUMP j    | k <- j                                                  | 1    |
| JPOS j    | If p_0 > 0 then k <- j else k <- k+1                    | 1    |
| JZERO j   | If p_0 = 0 then k <- j else k <- k+1                    | 1    |
| JUMPI i   | k <- p_i                                                | 1    |
| HALT      | Exit program execution                                  | 0    |
