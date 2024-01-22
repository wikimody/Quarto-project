import subprocess
from quarto_game.board import Board

# tworzymy tablicę argumentów i wykonujemy, zwracamy standardowe wyjście, zwrócone przez program
def execute_cpp(program_path : str, program_args : str) -> str:
    run_args = [program_path] + program_args.split(sep = " ")
    result = subprocess.run(run_args, capture_output=True, encoding='utf-8')
    return result.stdout


# przeglądamy tablicę i tworzymy napis, który odpowiada wyglądowi tablicy, a na końcu dopisujemy wybrany pionek
def generate_args(board : Board, piece_choice : int) -> str:
    result = board.format()
    result += hex(piece_choice)[2::].upper()
    return result

# napis dzielimy na pojedyncze znaki i wybieramy nas interesują
def receive_args(receive : str) -> list:
    tmp = list(receive)
    return [int(tmp[0]), int(tmp[1]), int(tmp[2], 16)]


def compile_cpp(cpp_name, executable_name):
        compile_command = f"g++ -o {executable_name} {cpp_name}"
        compilation_result = subprocess.run(compile_command)
        if compilation_result.returncode != 0:
            print(f"Compilation failed with error code {compilation_result}")
            exit()