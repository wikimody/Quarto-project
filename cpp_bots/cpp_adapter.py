import subprocess
import platform
from quarto_game.board import Board


def execute_cpp(program_path : str, program_args : str) -> str:
    run_args = [program_path] + program_args.split(sep = " ")

    if platform.system() == 'Linux':
        run_args = ['wine'] + run_args
    
    result = subprocess.run(run_args, capture_output=True, encoding='utf-8')
    return result.stdout


def generate_args(board : Board, piece_choice : int) -> str:
    result = ""
    for i in range(4):
        for j in range(4):
            if board[i][j].decimal() == -1: # place is empty
                result += 'p'
            else:
                result += hex(board[i][j].decimal)[2::]
    result += hex(piece_choice)[2::]
    return result


def receive_args(receive : str) -> list:
    tmp = receive.split(sep = '')
    return [int(tmp[0]), int(tmp[1]), int(tmp[2], 16)]


def compile_cpp(cpp_name, executable_name):
        compile_command = f"g++ -o {executable_name} {cpp_name}"
        compilation_result = subprocess.run(compile_command)
        if compilation_result.returncode != 0:
            print(f"Compilation failed with error code {compilation_result}")
            exit()