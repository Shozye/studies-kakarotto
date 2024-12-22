import os
import subprocess
from collections import defaultdict
import json
import sys
import time
from statistics import mean
from constants_helper_classes import *
from collections import defaultdict

WIN = "WIN"
LOSE = "LOSE"
DRAW = "DRAW"
WIN_ERROR = "WIN_ERROR"
LOSE_ERROR = "LOSE_ERROR"
BAD_PORT = "BAD_PORT"
UNEXPECTED_ERROR = "UNEXPECTED_ERROR"

CODE_TO_NAME = {
    "100": WIN,
    "200": LOSE,
    "300": DRAW,
    "400": WIN_ERROR,
    "500": LOSE_ERROR
}

OPPOSITE = {
    LOSE: WIN,
    WIN: LOSE,
    DRAW: DRAW,
    LOSE_ERROR: WIN_ERROR,
    WIN_ERROR: LOSE_ERROR
}

def get_inner_statistics():
    return {
        WIN:0,
        LOSE:0,
        DRAW:0,
        WIN_ERROR:0,
        LOSE_ERROR:0,
        BAD_PORT:0
    }

def get_inner_statistics2():
    return defaultdict(int)

def get_base_statistics():
    return {
        "1": get_inner_statistics2(),
        "2": get_inner_statistics2()
    }
    
class DirectoryManager:
    previous_path = os.getcwd()
    
    @staticmethod
    def enter(path: str):
        os.chdir(path)
    
    @staticmethod
    def go_back():
        os.chdir(DirectoryManager.go_back)

class Client:
    def __init__(self, name: str, run, player: int):
        self.name = name
        self.run_ = run
        self.player = player
    
    def run(self, PORT, DEPTH):
        return self.run_(PORT, DEPTH, self.player)

    
class Config:
    IP = "127.0.0.1"
    AMOUNT = 100 * 2
    DEBUG = len(sys.argv) >= 2
    PORT_START = 8500
    MAX_PORT = 9000
    DEPTH_START = 3
    
def write_to_file(text: str, path: str):
    with open(path, 'w+', encoding='utf-8') as file:
        file.write(text)

def json_dump(obj, path: str):
    write_to_file(json.dumps(obj, indent=4), path)


TIME_DATA = {
    "PLAY_GAME": [],
    "SOCKETING_CLOCK": [],
    "PLAYING_CLOCK": [],
    "FULL_PROGRAM_EXECUTION_START": 0,
    "FULL_PROGRAM_EXECUTION_END": 0,
    "SERVER_SOCKET_RECV_WAIT": [],
    "SERVER_SOCKET_SEND_WAIT": []
}
def print_time_info():
    time_taken = TIME_DATA["FULL_PROGRAM_EXECUTION"]
    print(f"EXEC TIME: {time_taken}s. {round(Config.AMOUNT/time_taken, 2)}game/s, {round(time_taken/Config.AMOUNT, 3)}s/game")
    print(f"GAMES TIME: {sum(TIME_DATA['PLAY_GAME'])}s, {round(mean(TIME_DATA['PLAY_GAME']), 3)}s/game")
    
    if TIME_DATA["PLAYING_CLOCK"]:
        socket = mean(TIME_DATA["SOCKETING_CLOCK"])
        game = mean(TIME_DATA["PLAYING_CLOCK"])
        full = socket+game
        server_recv_wait = mean(TIME_DATA["SERVER_SOCKET_RECV_WAIT"])
        server_send_wait = mean(TIME_DATA["SERVER_SOCKET_SEND_WAIT"])
        full = socket+game

        print("SERVER TIME RUNNING")
        print(f"CONNECT/SOCKET: {int(100*socket/full)}%")
        print(f"SERVER_SOCKET_RECV_WAIT: {int(100*server_recv_wait/full)}%")
        print(f"SERVER_SOCKET_SEND_WAIT: {int(100*server_send_wait/full)}%")
        print(f"OTHER: {int(100*(full-socket-server_recv_wait-server_send_wait )/ full)}%")
        
def parse_time_logs(time_log: str, server_playlog: str):
    recv, send = map(int, server_playlog.split(" ")[1:])
    socketing, playing = map(int, time_log.split(" ")[1:])
    
    TIME_DATA["SOCKETING_CLOCK"].append(socketing)
    TIME_DATA["PLAYING_CLOCK"].append(playing)
    TIME_DATA["SERVER_SOCKET_SEND_WAIT"].append(send)
    TIME_DATA["SERVER_SOCKET_RECV_WAIT"].append(recv)
    
def run_server(port):
    path_exec = "/home/base/Desktop/repos/studies-intro-artificial-intelligence/lab2/server/game_server"
    command = f"{path_exec} {Config.IP} {port}"
    return subprocess.Popen(
        command.split(),
        stdout=subprocess.PIPE
    ) 

def run_my_single_client(port, depth, player):
    path_exec = "/home/base/Desktop/repos/studies-intro-artificial-intelligence/lab2/TicTacToeExtended/target/scala-3.2.2/TicTacToeExtended-assembly-0.1.0-ASSEMBLY.jar"
    command = f"java -jar {path_exec} {Config.IP} {port} {player} {depth}"
    return subprocess.Popen(
        command.split(),
        stdout = subprocess.PIPE
    )

def run_random_strategy(port, depth, player):
    path_exec = "/home/base/Desktop/repos/studies-intro-artificial-intelligence/lab2/runners/TTTExtended-assembly-0.1.0-RandomStrategy.jar"
    command = f"java -jar {path_exec} {Config.IP} {port} {player} {depth}"
    return subprocess.Popen(
        command.split(),
        stdout = subprocess.PIPE
    )

def run_random_legal_strategy(port, depth, player):
    path_exec = "/home/base/Desktop/repos/studies-intro-artificial-intelligence/lab2/runners/TTTExtended-assembly-0.1.0-RandomLegalStrategy.jar"
    command = f"java -jar {path_exec} {Config.IP} {port} {player} {depth}"
    return subprocess.Popen(
        command.split(),
        stdout = subprocess.PIPE
    )
    
def run_minimax(port, depth, player):
    path_exec = "/home/base/Desktop/repos/studies-intro-artificial-intelligence/lab2/TicTacToeExtended/target/scala-3.2.2/TTTExtended-assembly-0.1.0-Simulation.jar"
    command = f"java -jar {path_exec} {Config.IP} {port} {player} {depth} minimax"
    return subprocess.Popen(
        command.split(),
        stdout = subprocess.PIPE
    )
    
def run_random_minimax(port, depth, player):
    path_exec = "/home/base/Desktop/repos/studies-intro-artificial-intelligence/lab2/TicTacToeExtended/target/scala-3.2.2/TTTExtended-assembly-0.1.0-Simulation.jar"
    command = f"java -jar {path_exec} {Config.IP} {port} {player} {depth} minimax-random"
    return subprocess.Popen(
        command.split(),
        stdout = subprocess.PIPE
    )
    
def run_game(
    PORT: str,
    DEPTH: int,
    CLIENT1: Client,
    CLIENT2: Client,
):
    
    proc_server = run_server(PORT)
    proc_c1 = CLIENT1.run(PORT, DEPTH)
    proc_c2 = CLIENT2.run(PORT, DEPTH)
    
    for proc in [proc_server, proc_c1, proc_c2]:
        proc.wait()
    
    
    stdout = proc_server.stdout.read().decode("utf-8")
    
    splitted = stdout.split("\n")
    messages = (list(filter(lambda x: "message" in  x, splitted)))
    client_messages = list(filter(lambda x: 'Client' in x, messages))
    
    result = {}
    if (len(client_messages) == 0):
        result[CLIENT1.name], result[CLIENT2.name] = BAD_PORT, BAD_PORT
    else:
        parse_time_logs(splitted[-1], splitted[-2])
        
        last_player = len(client_messages) % 2 + 1
        last_client, not_last_client = (CLIENT1, CLIENT2) if CLIENT1.player != last_player else (CLIENT2, CLIENT1)
        
        last_server_code = list(filter(lambda x: 'Server' in x, messages))[-1].split(" ")[-1]
        
        result[last_client.name] = CODE_TO_NAME.get(last_server_code, UNEXPECTED_ERROR)
        result[not_last_client.name] = OPPOSITE.get(result[last_client.name], UNEXPECTED_ERROR)
        
    return result, stdout, proc_c1.stdout.read().decode("utf-8")

def main():
    port = Config.PORT_START
    depth = Config.DEPTH_START
    CLIENT1 = Client("minimax", run_minimax, 1)
    CLIENT2 = Client("minimax-random", run_random_minimax, 2)
    
    test_data = { CLIENT1.name: get_base_statistics(), CLIENT2.name: get_base_statistics()}
    
    for i in range(Config.AMOUNT):
        CLIENT1.player, CLIENT2.player = CLIENT2.player, CLIENT1.player 
        
        play_game_time = time.time()
        result, stdout, proc_stdout = run_game(port, depth, CLIENT1, CLIENT2)
        TIME_DATA["PLAY_GAME"].append(time.time()-play_game_time)
        
        for client in [CLIENT1, CLIENT2]:
            test_data[client.name][str(client.player)][result[client.name]] += 1
        
        if port == Config.MAX_PORT:
            port = Config.PORT_START
        else:
            port += 1
        
        if Config.DEBUG:
            write_to_file(stdout, f"run_logs/LOG_{i}.log")
            write_to_file(proc_stdout, f"run_logs/LOG_{i}_minimax.log")
            json_dump(test_data, "test_data.json")
            
    
    json_dump(test_data, "test_data.json")
        

if __name__ == "__main__":
    TIME_DATA["FULL_PROGRAM_EXECUTION"] = time.time()
    
    if Config.DEBUG:
        os.makedirs("run_logs", exist_ok=True)
        
    main()
    
    TIME_DATA["FULL_PROGRAM_EXECUTION"] = time.time() - TIME_DATA["FULL_PROGRAM_EXECUTION"]
    print_time_info()
