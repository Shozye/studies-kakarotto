import os


class Logger:
    def __init__(self):
        self.logs_dir = "../logs"
        if not os.path.isdir(self.logs_dir):
            os.mkdir(self.logs_dir)
            os.mkdir(os.path.join(self.logs_dir, "run_-1"))

        max_index = max([int(x.split("_")[1]) for x in os.listdir(self.logs_dir)])
        index = max_index + 1
        self.index_dir = f"run_{str(index)}"
        os.mkdir(os.path.join(self.logs_dir, self.index_dir))

    def log(self, n, msg):
        with open(os.path.join(self.logs_dir, self.index_dir, f"{str(n)}.json"), 'w+') as file:
            file.write(msg)

    def full_log(self, msg):
        with open(os.path.join(self.logs_dir, self.index_dir, "full_log.json"), 'w+') as file:
            file.write(msg)
