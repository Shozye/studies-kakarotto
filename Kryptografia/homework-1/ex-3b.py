import json
import sys
from ex3help import base64url_to_long
from ex1 import RSA_CRT


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
    p, q, dp, dq, qi = list(map(base64url_to_long, [data['p'], data['q'], data['dp'], data['dq'], data['qi']]))
    print(RSA_CRT(x, p, q, dp, dq, qi))
