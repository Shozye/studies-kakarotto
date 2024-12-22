# Testcases schema
- All tests should be inside `test_.*` folder
- In a Test Folder there should be `config.json` file with schema specified below
- In a Test Folder there should be programs written in `.imp`
# Testcase Folder Example
```
/tests_maciek
|- config.json
|- test1.imp
|- test2.imp
|- test3.imp
```
# Config.json Schema
### Config.json
```json
[
    TestObject1, TestObject2, . . ., TestObjectN
]
```
### TestObject
```json
{
    "filename":           str,        // self explanatory
    "translated":         str,        // OPTIONAL. add filename of translated test
    "compilation": "ERROR" | "PASS",  // if it goes through compilation then PASS
    "runtime":     "ERROR" | "PASS",  // if i can run it gives output then PASS. If compilation is "ERROR" then runtime is "ERROR" too 
    "stdin":              str,        // what should i provide on entry
    "stdout":             "" ,        // expected stdout
    "description":        str         // what is happening in test
}
```
### Example
```json
[
    {
        "filename": "test1.imp",
        "compilation": "PASS",
        "runtime": "PASS",
        "stdin": "7\n11\n9",
        "stdout": "1\n1\n0",
        "description": "Implementation and execution algorithm to check if number is prime"
    },
    {
        "filename": "test2.imp",
        "compilation": "ERROR",
        "runtime": "ERROR",
        "stdin": "",
        "stdout": "",
        "description": "Double declaration of the same variable"
    },
    {
        "filename": "test3.imp",
        "compilation": "PASS",
        "runtime": "PASS",
        "stdin": "16\n12",
        "stdout": "4",
        "description": "Implementation and execution GCD algorithm"
    },
]
```
### Default values:
```json
{
    "translated": "",
    "compilation": "ERROR",
    "runtime": "ERROR",
    "stdin": "",
    "stdout": "",
    "description": "Default Description"
}
```