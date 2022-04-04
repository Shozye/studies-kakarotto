from graph_creator import *

def main():
    graphLine = load_from_saved("line.json")
    graphCircle = load_from_saved("circular.json")
    graphCircleCross = load_from_saved("upgraded_circular_topology.json")
    graphDoubleCircle = load_from_saved("double_circular.json")
    graphBestRandom = load_from_saved("best_random.json")

if __name__ == "__main__":
    main()