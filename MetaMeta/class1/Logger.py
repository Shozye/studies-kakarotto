import logging
import os
import shutil


def setup_logging(level=logging.INFO):
    LOGS = "logs"
    if os.path.isdir(LOGS):
        shutil.rmtree(LOGS)
    os.mkdir(LOGS)

    for name in ["basic", "accelerate", "stagnation", "cycled", "long_term_memory", "two_opt"]:
        full_name = name if name == "two_opt" else name + "_taboo"
        logger = logging.getLogger(name)
        logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh = logging.FileHandler(os.path.join(LOGS, f"{full_name}.log"))
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
