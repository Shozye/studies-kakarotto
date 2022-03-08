import sys
from ex1 import RSA_CRT


def printUsageAndExit():
    print("""Usage:
    python3 ex-2b x p q dp dq qi
    where x p q dp dq qi are parameters of RSA_CRT function.""")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 7:
        printUsageAndExit()
    x, p, q, dp, dq, qi = list(map(int, list(sys.argv[1:])))
    print(RSA_CRT(x, p, q, dp, dq, qi))
