import os

class CppAdapter:
    @staticmethod
    def compile_cpp(cpp_name, executable_name):
        os.popen(f"g++ -o {executable_name} {cpp_name}")

    @staticmethod
    def execute_cpp(executable_program, executable_input):
        return os.popen(f"./{executable_program} {executable_input}").read()

if __name__ == "__main__":
    CppAdapter.compile_cpp("example.cpp", "example.exe")
    CppAdapter.execute_cpp("example.exe", "Adapter")
