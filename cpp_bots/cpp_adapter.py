import subprocess
import platform

def execute_cpp(program_path : str, program_args : str) -> str:
    run_args = [program_path] + program_args.split(sep = " ")

    if platform.system() == 'Linux':
        run_args = ['wine'] + run_args
    
    result = subprocess.run(run_args, capture_output=True)
    return result.stdout
