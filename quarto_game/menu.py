from interactions.console import Console


class Menu:
    def __init__(self, title="Quarto Game. Menu:", exit_option="Wyjdź z gry"):
        self.title = title
        self.exit_option = exit_option
        self.options = []

    def add_option(self, description, function):
        self.options.append((description, function))

    def display(self):
        Console.clear_view()
        Console.output(f"\n{self.title}")
        for index, option in enumerate(self.options):
            Console.output(f"{index + 1}. {option[0]}")
        Console.output(f"0. {self.exit_option}")

    def run(self):
        while True:
            self.display()
            choice = Console.input_number_in_range(f"Wybierz opcję (0-{len(self.options)}): ", 0, len(self.options))
            if choice == 0:
                Console.output(f"{self.exit_option}.")
                break
            self.options[choice - 1][1]()
