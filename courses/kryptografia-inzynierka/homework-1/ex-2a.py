import sys
from ex1 import RSA


def printUsageAndExit():
    print("""Usage:
    python3 ex-2a x N e
    where x N e are parameters of RSA function.""")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        printUsageAndExit()
    x, N, e = list(map(int, list(sys.argv[1:])))
    print(RSA(x, N, e))
