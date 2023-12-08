import os

class CppAdapter:
    @staticmethod
    def compile_cpp(cpp_name, executable_name):
        compile_command = f"g++ -o {executable_name} {cpp_name}"
        compilation_result = os.system(compile_command)
        if compilation_result != 0:
            print(f"Compilation failed with error code {compilation_result}")
            exit()

    @staticmethod
    def execute_cpp(executable_program, executable_input):
        execution_result = os.popen(f"./{executable_program} {executable_input}").read()
        return execution_result

if __name__ == "__main__":
    CppAdapter.compile_cpp("example.cpp", "example.exe")
    out = CppAdapter.execute_cpp("example.exe", "Adapter\)")
    print(out)
