import os.path

from z3_main import main


def run():
    dir = "pictures"
    new_dir = "zad3"
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    filenames = [f"example{i}" for i in range(4)]
    for filename in filenames:
        path_to_output_dir = os.path.join(new_dir, filename)
        if not os.path.isdir(path_to_output_dir):
            os.mkdir(path_to_output_dir)
        for i in range(1, 8):
            path_to_output_file = os.path.join(path_to_output_dir, f"{filename}_{i}.tga")
            main(os.path.join(dir, f"{filename}.tga"), path_to_output_file, i)


if __name__ == "__main__":
    run()
