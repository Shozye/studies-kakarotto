import json
import sys
from ex3help import base64url_to_long
from ex1 import RSA


def printUsageAndExit(text=""):
    if text != "":
        text = text + "\n"
    print(f"""{text}Usage:
    python3 ex-3a x filename
    filename is a relative path to file .jwk structured for RSA public
    x is message to encrypt""")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        printUsageAndExit("Wrong amount of arguments")
    filename = sys.argv[2]
    x = int(sys.argv[1])

    with open(filename) as file:
        try:
            data = dict(json.loads(file.read()))
        except Exception:
            printUsageAndExit("File not Jsonable to dictionary")
    N, e = list(map(base64url_to_long, [data["n"], data["e"]]))
    print(RSA(x, N, e))
